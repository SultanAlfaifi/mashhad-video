'use strict';
const fs=require('fs');
const sharp=require(process.env.SHARP_PATH||'sharp');
const jsQR=require(process.env.JSQR_PATH||'jsqr');
const file=process.argv[2];
if(!file)throw Error('Pass a decoded video frame or QR image');
const expected='https://github.com/SultanAlfaifi/mashhad-video';
(async()=>{
 const results=[];
 for(const width of [1920,1280,960]){
  const {data,info}=await sharp(file).resize({width,withoutEnlargement:true}).ensureAlpha().raw().toBuffer({resolveWithObject:true});
  const decoded=jsQR(new Uint8ClampedArray(data),info.width,info.height,{inversionAttempts:'dontInvert'});
  const result={width:info.width,height:info.height,decoded:decoded?.data||null,passed:decoded?.data===expected};results.push(result);
 }
 console.log(JSON.stringify({file,expected,results},null,2));
 if(results.some(r=>!r.passed))process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1});
