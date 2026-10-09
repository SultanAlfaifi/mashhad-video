# إعلان مَشْهَد — مؤثرات فقط

28 ثانية، 1920×1080، 30 إطارًا، مع QR للمستودع وخاتمة ثابتة للمسح. الصوت مؤثرات أصلية مولّدة إجرائيًا: نفحات انتقال ونقرات مكتومة وبيئة غير موسيقية. لا تتضمن موسيقى أو عينات صوتية خارجية.

## إعادة الإخراج

تحتاج Node.js مع Playwright/Chromium، وFFmpeg/ffprobe، وPython مع NumPy وPillow وReportLab. المتطلبات معلنة في `package.json` و`requirements.txt`؛ أوامر الرندر لا تنفذ تثبيتًا تلقائيًا. يمكن الاستفادة من تثبيتات موجودة عبر `PLAYWRIGHT_PATH` و`SHARP_PATH` و`JSQR_PATH` و`FFMPEG`.

احصل على [خط ثمانية من مصدره الرسمي](https://font.thmanyah.com/)، واضبط `THMANYAH_FONT_DIR` إلى مجلد `thmanyahsans` الذي يحوي `woff2/`. الملفات لا تُنشر مع المثال وفق [ترخيص ثمانية](https://font.thmanyah.com/licenses).

```powershell
$env:THMANYAH_FONT_DIR = 'D:/Fonts/thmanyah typeface/thmanyahsans'
python make_qr.py
python audio/compose_sfx.py
node render.cjs proof
node render.cjs full
node encode.cjs mashhad-ad-sfx.mp4
```

تظهر الصور في `frames/`، ولا يقبل الترميز الكتابة فوق فيديو سابق. لإعادة تصوير مقطع محدد: `node render.cjs range 630 840`؛ الحد الأخير غير مشمول. تعتمد الصورة على رقم الإطار، فلا يتطلب التصوير تشغيل المشاهد بالترتيب.

`film.js` يحتوي النصوص والحركة. QR في `assets/repository-qr.png` مولّد بواسطة `make_qr.py`، ويشير مباشرةً إلى `https://github.com/SultanAlfaifi/mashhad-video`. تتحقق أداة `verify-qr.cjs` من صورة إطار مفكوك من الفيديو بدقات متعددة باستخدام jsQR. المؤثرات في `audio/compose_sfx.py` مع قياسات ومنشأ كل إشارة في `audio/audio-report.json`.

هذه الرسوم والنصوص البرمجية والمؤثرات الأصلية © 2026 Sultan Alfaifi، تحت ترخيص المشروع MIT. المكتبات الخارجية وخط ثمانية تحت تراخيصها المستقلة؛ راجع إشعارات الحقوق في جذر المستودع. لا تُرفق خطوط أو محركات أو مكتبات مورّدة في المثال.
