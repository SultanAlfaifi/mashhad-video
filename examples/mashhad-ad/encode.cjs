'use strict';
const path=require('path'),fs=require('fs'),{spawnSync}=require('child_process');
const root=__dirname,output=path.resolve(process.argv[2]||path.join(root,'mashhad-ad.mp4'));
if(fs.existsSync(output))throw Error('Output already exists; choose a new path: '+output);
const args=['-hide_banner','-loglevel','error','-n','-framerate','30','-i',path.join(root,'frames/%05d.png'),'-i',path.join(root,'audio/mashhad-sfx.wav'),
 '-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','slow','-crf','17','-pix_fmt','yuv420p',
 '-vf','scale=in_range=full:out_range=tv:out_color_matrix=bt709,setparams=range=limited:color_primaries=bt709:color_trc=bt709:colorspace=bt709',
 '-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv',
 '-c:a','aac','-b:a','256k','-ar','48000','-movflags','+faststart','-frames:v','840','-t','28',output];
const result=spawnSync(process.env.FFMPEG||'ffmpeg',args,{stdio:'inherit'});
if(result.error)throw result.error;
if(result.status!==0)process.exit(result.status||1);
fs.writeFileSync(path.join(root,'encoding-command.json'),JSON.stringify({executable:process.env.FFMPEG||'ffmpeg',arguments:args,output},null,2));
console.log(output);
