'use strict';
const canvas=document.querySelector('canvas'), c=canvas.getContext('2d',{alpha:false});
const W=1920,H=1080, P='#F2EDE3', I='#14201C', O='#EC603F', S='#AFBAA7';
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const mix=(a,b,p)=>a+(b-a)*p;
const ease=x=>{x=clamp(x);return x*x*x*(x*(x*6-15)+10)};
const out=x=>1-Math.pow(1-clamp(x),4);
const progress=(t,a,b)=>clamp((t-a)/(b-a));
function rgba(hex,a){return 'rgba('+parseInt(hex.slice(1,3),16)+','+parseInt(hex.slice(3,5),16)+','+parseInt(hex.slice(5,7),16)+','+clamp(a)+')'}
function round(x,y,w,h,r,fill,stroke,lw=2){c.beginPath();c.roundRect(x,y,w,h,r);if(fill){c.fillStyle=fill;c.fill()}if(stroke){c.strokeStyle=stroke;c.lineWidth=lw;c.stroke()}}
function line(x1,y1,x2,y2,color,width=2,alpha=1){c.save();c.globalAlpha*=alpha;c.strokeStyle=color;c.lineWidth=width;c.beginPath();c.moveTo(x1,y1);c.lineTo(x2,y2);c.stroke();c.restore()}
function circle(x,y,r,fill,stroke,lw=2){c.beginPath();c.arc(x,y,Math.max(.01,r),0,Math.PI*2);if(fill){c.fillStyle=fill;c.fill()}if(stroke){c.strokeStyle=stroke;c.lineWidth=lw;c.stroke()}}
function text(value,x,y,size=80,weight=700,color=I,align='center',alpha=1){
 c.save();c.globalAlpha*=clamp(alpha);c.fillStyle=color;c.font=weight+' '+size+'px Thmanyah';c.textAlign=align;c.textBaseline='middle';c.direction=/[\u0600-\u06FF]/.test(value)?'rtl':'ltr';c.fillText(value,x,y);c.restore();
}
function enter(value,x,y,size,weight,color,t,start,duration=.65,align='center'){
 const e=out(progress(t,start,start+duration));text(value,x,y+55*(1-e),size,weight,color,align,e);
}
function corners(x,y,w,h,len,color=O,lw=5,p=1){
 c.save();c.strokeStyle=color;c.lineWidth=lw;c.lineCap='square';c.beginPath();
 for(const [px,py,sx,sy] of [[x,y,1,1],[x+w,y,-1,1],[x+w,y+h,-1,-1],[x,y+h,1,-1]]){
  c.moveTo(px,py+sy*len*p);c.lineTo(px,py);c.lineTo(px+sx*len*p,py);
 }c.stroke();c.restore();
}
function logo(x,y,s,color=O,alpha=1){c.save();c.globalAlpha*=alpha;corners(x-s/2,y-s/2,s,s,s*.26,color,s*.055);c.restore()}
function chrome(t,dark=false,section='',accent=O){
 const fg=dark?P:I;
 logo(116,91,44,accent);text('مَشْهَد',163,93,33,700,fg,'left');
 if(section)text(section,1802,93,24,500,rgba(fg,.65),'right');
 line(94,980,1826,980,fg,1,.18);
 const p=clamp(t/28);line(94,980,94+1732*p,980,accent,3);
 text('من الفكرة إلى الفيديو',1808,1018,22,400,rgba(fg,.6),'right');
 text('MASHHAD  /  CODEX + CLAUDE',96,1018,17,500,rgba(fg,.6),'left');
}
function bg(color){c.fillStyle=color;c.fillRect(0,0,W,H)}
function grid(alpha=.1,color=I,step=90,offset=0){
 c.save();c.strokeStyle=color;c.lineWidth=1;c.globalAlpha=alpha;c.beginPath();
 for(let x=offset%step;x<W;x+=step){c.moveTo(x,0);c.lineTo(x,H)}
 for(let y=offset%step;y<H;y+=step){c.moveTo(0,y);c.lineTo(W,y)}c.stroke();c.restore();
}
function seed(x,y,r,t){
 c.save();c.translate(x,y);c.rotate(t*.23);circle(0,0,r,O);
 c.strokeStyle=rgba(P,.8);c.lineWidth=Math.max(1.5,r*.023);c.beginPath();
 c.ellipse(0,0,r*.62,r*.97,-.6,0,Math.PI*2);c.stroke();
 c.beginPath();c.ellipse(0,0,r*.29,r*.96,-.6,0,Math.PI*2);c.stroke();
 c.restore();
}
function cube(x,y,size,angle,color,alpha=1){
 const pts=[]; const ca=Math.cos(angle),sa=Math.sin(angle),cb=Math.cos(.55),sb=Math.sin(.55);
 for(let z of [-1,1])for(let yy of [-1,1])for(let xx of [-1,1]){
 const a=xx*ca+z*sa,b=-xx*sa+z*ca, Y=yy*cb-b*sb,Z=yy*sb+b*cb;
 const scale=4/(4-Z*.5);pts.push([x+a*size*scale,y+Y*size*scale,Z]);}
 c.save();c.globalAlpha*=alpha;
 for(const [a,b] of [[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],[2,6],[3,7],[4,5],[4,6],[5,7],[6,7]])line(...pts[a].slice(0,2),...pts[b].slice(0,2),color,2.8,.5+(pts[a][2]+2)*.1);
 for(const pt of pts)circle(pt[0],pt[1],5,color);c.restore();
}
function iris(t,start,duration,color,x=960,y=540){
 const p=ease(progress(t,start,start+duration));if(p<=0)return;
 circle(x,y,p*2300,color);
}
function sceneIdea(t){
 bg(P);grid(.045,I,96,-t*8);
 const a=out(progress(t,0,.85));
 seed(mix(100,490,a),540,100+5*Math.sin(t*2),t);
 const cp=out(progress(t,.25,1.2));corners(270,310,440,460,58,I,4,cp);
 line(710,540,900,540,I,1.5,cp*.3);
 enter('فكرة واحدة.',1700,456,154,900,I,t,.28,.7,'right');
 enter('تستحق مشهدًا مختلفًا.',1700,652,76,500,I,t,.8,.7,'right');
 text('01 / الفكرة',490,835,26,500,rgba(I,.5),'center',out(progress(t,.7,1.2)));
 chrome(t,false,'كلّ شيء يبدأ هنا');
 const z=ease(progress(t,2.52,3));if(z>0){circle(490,540,z*2250,I);}
}
function sceneBrand(t){
 const q=t-3;bg(I);grid(.065,P,120);
 // Expanding concentric film frames pull the eye into the central title.
 for(let k=0;k<4;k++){
 const p=out(progress(q,0+k*.09,1.1+k*.09));
 const w=mix(170,1460+k*230,p),h=mix(90,490+k*165,p);
 corners(960-w/2,520-h/2,w,h,65+k*8,k===0?O:rgba(P,.1),k===0?5:1,p);
 }
 enter('مَشْهَد',960,500,260,900,P,q,.1,.8);
 enter('مهارة إخراج الفيديو',960,737,53,500,P,q,.55,.75);
 enter('Codex  ·  Claude Code',960,819,29,500,S,q,.72,.6);
 text('MOTION, WITH INTENTION.',960,252,22,500,rgba(P,.55),'center',out(progress(q,.6,1)));
 chrome(t,true,'الفكرة تجد لغتها');
 // A flat shutter continues the frame motif into the next composition.
 const p=ease(progress(q,2.55,3));if(p>0){round(0,1080*(1-p),1920,1080,0,P);}
}
function panel(x,y,w,h,fill,rot,draw){c.save();c.translate(x+w/2,y+h/2);c.rotate(rot);c.shadowColor='rgba(20,32,28,.14)';c.shadowBlur=24;c.shadowOffsetY=20;round(-w/2,-h/2,w,h,20,fill);c.shadowBlur=0;c.shadowOffsetY=0;c.beginPath();c.roundRect(-w/2,-h/2,w,h,20);c.clip();draw(w,h);c.restore();}
function sceneCraft(t){
 const q=t-6;bg(P);
 enter('فكّر. شكّل. حرّك.',960,269,121,900,I,q,.15,.7);
 const cards=[{x:210,fill:I,r:-.045},{x:705,fill:O,r:.025},{x:1200,fill:S,r:.045}];
 cards.forEach((v,j)=>{
 const p=out(progress(q,.22+j*.15,1+j*.15));const yy=mix(1120,440,p)+Math.sin(q*1.6+j)*6;
 panel(v.x,yy,510,350,v.fill,v.r*(1-ease(progress(q,2.7,3.65))), (w,h)=>{
 if(j===0){text('Aa',0,-42,125,900,P);text('حروف تصنع المعنى',0,99,36,500,P);line(-180,40,180,40,O,4);}
 if(j===1){const tt=q*.9;for(let k=0;k<5;k++){c.save();c.translate(Math.sin(tt+k*.1)*28,0);c.rotate(tt*.15+k*.14);c.strokeStyle=rgba(I,.18+k*.15);c.lineWidth=3; c.strokeRect(-84-k*13,-84-k*13,168+k*26,168+k*26);c.restore();}circle(0,0,21,P);}
 if(j===2){cube(0,-25,79,q*.65,I);text('عمق يخدم الفكرة',0,130,29,500,I);}
 });
 });
 // One designed path joins the individual disciplines.
 const pathP=out(progress(q,1.6,2.6));line(414,858,414+1092*pathP,858,I,1.5,.35);
 for(let k=0;k<3;k++)circle(414+546*k,858,5+2*Math.sin(q*2+k),O);
 chrome(t,false,'إخراج • حركة • تفاصيل');
 const p=ease(progress(q,3.55,4));if(p>0)round(0,0,1920*p,1080,0,I);
}
function sceneEngines(t){
 const q=t-10;bg(I);grid(.045,P,96);
 enter('أدوات متعددة.',1792,380,119,900,P,q,.1,.75,'right');
 enter('رؤية واحدة.',1792,558,119,900,O,q,.48,.75,'right');
 enter('كلّ أداة في مكانها.',1785,740,42,500,S,q,1,.65,'right');
 const cx=570,cy=536,collapse=ease(progress(q,2.5,3.5));
 const names=['Remotion','GSAP','Blender','Manim'];
 for(let k=0;k<4;k++){
 const ang=k*Math.PI/2+q*.15-.55;
 const rx=mix(330,175,collapse),ry=mix(250,128,collapse);
 const x=cx+Math.cos(ang)*rx,y=cy+Math.sin(ang)*ry;
 line(cx,cy,x,y,P,1,.28);
 c.save();c.setLineDash([4,12]);c.strokeStyle=rgba(P,.17);c.lineWidth=1;c.beginPath();c.ellipse(cx,cy,rx,ry,0,0,Math.PI*2);c.stroke();c.restore();
 const a=out(progress(q,.25+k*.1,.8+k*.1))*(1-collapse*.68);
 c.save();c.globalAlpha=a;round(x-91,y-32,182,64,32,I,rgba(P,.4),1);text(names[k],x,y+2,27,500,P);c.restore();
 const flow=(q*.55+k*.2)%1;circle(mix(x,cx,flow),mix(y,cy,flow),4,O);
 }
 const lp=out(progress(q,.1,1));round(cx-119,cy-89,238,178,27,O);
 logo(cx,cy,94,I,lp);corners(cx-143,cy-113,286,226,22,P,2,collapse);
 chrome(t,true,'تنسيق واحد للمشهد');
 const p=ease(progress(q,3.55,4));if(p>0)circle(cx,cy,p*2250,P);
}
function sceneArabic(t){
 const q=t-14;bg(P);
 enter('عربي، كما ينبغي.',960,279,83,700,I,q,.08,.65);
 const p=out(progress(q,.15,.95));
 line(190,640,1730,640,I,1,.16);line(190,443,1730,443,I,1,.10);
 for(let x=280;x<=1660;x+=138)line(x,418,x,682,I,1,.065);
 // Reveal the complete shaped run through a geometric mask, never split letters.
 c.save();c.beginPath();c.rect(1860-1800*p,364,1800*p,360);c.clip();
 text('وضوحٌ يتحرّك.',960,550,194,900,I);c.restore();
 const u=out(progress(q,.85,1.8));round(1520-1120*u,717,1120*u,12,6,O);
 const scan=progress(q,1.1,2.4);if(scan>0&&scan<1){circle(mix(1550,360,scan),723,22,O);}
 enter('خطٌ واضح. إيقاعٌ محسوب.',960,825,40,500,rgba(I,.66),q,1.4,.6);
 chrome(t,false,'حروف متصلة • معنى واضح');
 const z=ease(progress(q,3.55,4));if(z>0){round(0,0,W,H*z,0,O);}
}
function sceneFinish(t){
 const q=t-18;bg(O);
 const gather=ease(progress(q,.45,1.4));
 const items=[[-480,-.13,P], [0,.045,I],[480,.13,S]];
 items.forEach(([off,rot,color],k)=>{
 const x=960+off*(1-gather),y=mix(670,625,gather);
 panel(x-280,y-152,560,304,color,rot*(1-gather),(w,h)=>{
 if(k===0){text('فكرة',0,-10,100,900,I);circle(-160,95,14,O)}
 if(k===1){cube(0,-5,79,q*.6,P);}
 if(k===2){seed(0,0,78,q);}
 });
 });
 if(gather>.2){const a=out(progress(q,1.15,1.65));c.save();c.globalAlpha=a;round(680,473,560,304,20,I);corners(708,501,504,248,30,P,3);text('مَشْهَد',960,622,124,900,P);c.restore();}
 enter('من الفكرة',960,226,91,700,I,q,.05,.6);
 enter('إلى الفيديو.',960,346,112,900,I,q,.25,.6);
 chrome(t,false,'الفكرة أصبحت مشهدًا',I);
 const z=ease(progress(q,2.5,3));if(z>0)round(0,1080*(1-z),1920,1080,0,I);
}
function sceneEnd(t){
 const q=t-21;bg(I);
 const p=out(progress(q,0,.8));
 logo(640,239,78,O,p);
 enter('مَشْهَد',640,450,218,900,P,q,.03,.7);
 enter('ابدأ بفكرتك.',640,652,62,500,P,q,.4,.6);
 const a=out(progress(q,.6,1));
 text('Codex  ·  Claude Code',640,759,35,500,S,'center',a);
 // QR is fully opaque and stationary from 22 seconds through the last frame.
 if(q>=.6){
  text('امسح وابدأ',1468,254,42,700,P);
  round(1225,314,486,486,22,'#FFFFFF');
  c.imageSmoothingEnabled=false;c.drawImage(window.repoQr,1222,311,492,492);c.imageSmoothingEnabled=true;
  text('github.com',1468,852,27,500,S);
  text('SultanAlfaifi/mashhad-video',1468,903,30,700,P);
 }
 text('MIT  ·  © 2026 Sultan Alfaifi',960,1013,22,400,rgba(P,.58),'center',a);
 // Hold the completed lockup through the last frame; no accidental black tail.
}
window.renderFrame=function(frame){
 const t=clamp(frame,0,839)/30;
 c.setTransform(1,0,0,1,0,0);c.globalAlpha=1;c.lineCap='butt';c.lineJoin='round';
 if(t<3)sceneIdea(t);else if(t<6)sceneBrand(t);else if(t<10)sceneCraft(t);else if(t<14)sceneEngines(t);else if(t<18)sceneArabic(t);else if(t<21)sceneFinish(t);else sceneEnd(t);
 window.currentFrame=frame;return true;
};
const qrReady=new Promise((resolve,reject)=>{const im=new Image();im.onload=()=>{window.repoQr=im;resolve()};im.onerror=()=>reject(Error('QR asset failed'));im.src='/assets/repository-qr.png'});
window.ready=Promise.all([...([400,500,700,900].map(w=>document.fonts.load(w+' 80px Thmanyah','مَشْهَد Codex Claude'))),qrReady]).then(async()=>{await document.fonts.ready;for(const w of[400,500,700,900])if(!document.fonts.check(w+' 80px Thmanyah'))throw Error('Missing font '+w);window.renderFrame(0);return true});
if(new URLSearchParams(location.search).has('play'))window.ready.then(()=>{const start=performance.now();function tick(now){window.renderFrame(Math.min(839,Math.floor((now-start)*.03)));if(now-start<28000)requestAnimationFrame(tick)}requestAnimationFrame(tick)});
