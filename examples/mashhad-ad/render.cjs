'use strict';
const fs=require('fs'),path=require('path'),http=require('http'),{spawn}=require('child_process');
const root=__dirname;
const playwrightPath=process.env.PLAYWRIGHT_PATH||'playwright';
const {chromium}=require(playwrightPath);
if(!process.env.THMANYAH_FONT_DIR)throw Error('Set THMANYAH_FONT_DIR to your locally licensed Thmanyah Sans folder. Get the font from https://font.thmanyah.com/');
const supplied=path.resolve(process.env.THMANYAH_FONT_DIR);
const fontRoot=[supplied,path.join(supplied,'woff2'),path.join(supplied,'thmanyahsans/woff2')].find(p=>fs.existsSync(path.join(p,'thmanyahsans-Regular.woff2')));
if(!fontRoot)throw Error('Thmanyah Sans WOFF2 files not found in the configured folder');
const mode=process.argv[2]||'proof';
const framesDir=path.join(root,'frames');
const proofsDir=path.join(root,'proofs');
const errors=[];
const mime={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.woff2':'font/woff2','.png':'image/png'};
const server=http.createServer((req,res)=>{
 const pathname=new URL(req.url,'http://localhost').pathname;
 let file;
 if(pathname.startsWith('/fonts/')){const name=pathname.split('/').pop();if(!/^thmanyahsans-(Regular|Medium|Bold|Black)\.woff2$/.test(name)){res.writeHead(404);return res.end()}file=path.join(fontRoot,name)}
 else if(pathname==='/'||pathname==='/film.html')file=path.join(root,'film.html');
 else if(pathname==='/film.js')file=path.join(root,'film.js');
 else if(pathname==='/assets/repository-qr.png')file=path.join(root,'assets/repository-qr.png');
 else {res.writeHead(404);return res.end()}
 try{res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream','Cache-Control':'no-store'});res.end(fs.readFileSync(file))}catch(e){res.writeHead(500);res.end(String(e));}
});
async function run(){
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const url='http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch({headless:true});
 try{
 const samples=[45,140,246,336,474,567,597,651,690,750,839];
 let indices;
 if(mode==='full')indices=Array.from({length:840},(_,i)=>i);
 else if(mode==='range'){
 const start=Number(process.argv[3]),end=Number(process.argv[4]);
 if(!Number.isInteger(start)||!Number.isInteger(end)||start<0||end>840||end<=start)throw Error('range requires integer start end within [0,840)');
 indices=Array.from({length:end-start},(_,i)=>start+i);
 }else if(mode==='proof')indices=samples;else throw Error('Use proof, full, or range START END');
 const dir=mode==='proof'?proofsDir:framesDir;fs.mkdirSync(dir,{recursive:true});
 let next=0,done=0;const start=Date.now();
 await Promise.all(Array.from({length:mode==='proof'?2:4},async()=>{
 const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
 page.on('pageerror',e=>errors.push(String(e)));page.on('requestfailed',r=>errors.push(r.url()+' '+r.failure()?.errorText));
 await page.goto(url,{waitUntil:'load'});await page.evaluate(()=>window.ready);
 while(next<indices.length){const frame=indices[next++];await page.evaluate(f=>window.renderFrame(f),frame);await page.screenshot({path:path.join(dir,String(frame).padStart(5,'0')+'.png'),type:'png',animations:'disabled'});done++;if(done%60===0)console.log(JSON.stringify({done,total:indices.length,elapsed_seconds:Math.round((Date.now()-start)/1000)}));}
 await page.close();
 }));
 fs.writeFileSync(path.join(root,mode+'-render.json'),JSON.stringify({mode,frames:indices,browser:browser.version(),errors,elapsed_seconds:(Date.now()-start)/1000,font_weights:[400,500,700,900]},null,2));
 if(errors.length)throw Error(errors.join('\n'));
 console.log(JSON.stringify({status:'rendered',mode,frames:indices.length,seconds:(Date.now()-start)/1000}));
 }finally{await browser.close();server.close();}
}
run().catch(e=>{console.error(e);server.close();process.exitCode=1});
