<div align="center">

# مَشْهَد · Mashhad

**من الفكرة إلى الفيديو — مهارة إخراج موشن قرافيك لـ Codex وClaude Code.**

[![مَشْهَد — إعلان دون موسيقى](docs/media/poster.jpg)](docs/media/mashhad-ad-sfx-1080p.mp4)

[شاهد الإعلان](docs/media/mashhad-ad-sfx-1080p.mp4) · [المهارة](skills/mashhad-video/SKILL.md) · [الحقوق والمصادر](THIRD_PARTY_NOTICES.md) · [English](#english)

</div>

مَشْهَد تجمع توجيه الإخراج، اختيار الأدوات، بناء المشاهد، تنسيق الصوت ومراجعة النتيجة في مهارة واحدة. تختار مسارًا مناسبًا للمشروع، وتحمل تفاصيله عند الحاجة. المحركات نفسها متطلبات منفصلة وليست مضمّنة.

- **صوت بلا موسيقى افتراضيًا:** مؤثرات انتقال وحركة وأجواء غير موسيقية، مع مصدر أو ترخيص موثق لكل مادة صوتية. لا ألحان أو تآلفات أو إيقاعات موسيقية، إلا بطلب صريح لاحق.
- **تعليق عربي اختياري:** مسار ElevenLabs يحترم الصوت الذي تختاره، ويضبط المشاهد وفق التسجيل الفعلي، مع فصل التعليق عن المؤثرات.
- **عربية مقروءة:** اتجاه صحيح، حروف متصلة، تشكيل واضح، وثمانية Sans خيار مفضّل عند توفره.
- **محرك رئيسي واحد:** Remotion أو HyperFrames أو Motion Canvas وغيرها، مع محركات متخصصة حين تفيد اللقطة.
- **تسليم قابل للمراجعة:** توقيت بالإطارات، عقود تبادل الصور والصوت، فحص فيديو، وتمييز واضح بين ما رُندر وما روجع.
- **توافق المضيف:** تعليمات مشتركة لـ Codex وClaude Code؛ العمل المتتابع متاح، ولا تحتاج أدوات تعاون خاصة بأحدهما.

## التثبيت

Python 3.10+ وGit يكفيان لنسخ المهارة. لا يثبّت الأمر التالي أي محرّك فيديو أو تطبيق أو خدمة مدفوعة.

```sh
git clone https://github.com/SultanAlfaifi/mashhad-video.git
cd mashhad-video
python tools/install.py --agent both
```

اختر `--agent codex` أو `--agent claude` لتثبيتها في أحدهما فقط. للتثبيت داخل مشروع:

```sh
python tools/install.py --agent both --scope project --project /path/to/your/project
```

| المضيف | المسار الشخصي | الاستدعاء |
| --- | --- | --- |
| Codex | `~/.agents/skills/mashhad-video` | `$mashhad-video` |
| Claude Code | `~/.claude/skills/mashhad-video` | `/mashhad-video` |

المثبّت يرفض استبدال مهارة موجودة، ويتعرف على مسار Codex الأقدم `~/.codex/skills` عند وجود النسخة هناك، لتجنب تكرارها. استخدم `--dry-run` لمعاينة الوجهات. احفظ تخصيصات نسختك قبل استبدالها. واجهة `agents/openai.yaml` اختيارية خاصة بـCodex، بينما النواة واحدة.

في Claude/Cowork السحابي، مجلد المهارات المحلي لا ينتقل تلقائيًا؛ فعّل المهارة عبر إدارة المهارات في حسابك، وتأكد من توفر أدوات التنفيذ في البيئة. انظر [وثائق Claude الرسمية](https://code.claude.com/docs/en/skills) و[وثائق Codex الرسمية](https://developers.openai.com/codex/skills).

## مثال طلب

```text
اصنع إعلانًا عربيًا من 20 ثانية لمنتجي، بخط ثمانية Sans.
استخدم مؤثرات انتقال وأجواء خلفية فقط، دون موسيقى.
اختر المحرك المناسب، سلّم الفيديو والمصدر، واذكر الفحوص المنفّذة.
```

## تعليق صوتي مع ElevenLabs

عند طلب تعليق أو مؤثرات مولّدة، تستخدم مَشْهَد [مسار ElevenLabs الاختياري](skills/mashhad-video/references/elevenlabs-audio.md). تعطي الأولوية للإضافة المتصلة في المضيف؛ لا تحتاج مفتاح API منفصلًا لهذا المسار. تشغيل API داخل تطبيق مستقل له إعداداته الخاصة. توفر الأدوات والأصوات والتكلفة يعتمد على الاتصال والحساب، والخدمة ليست مضمّنة في المهارة.

يمكنك تحديد `voice_id` بعينه. يُكتب النص المنطوق مستقلًا عن نص الشاشة، وتُقاس مدة التسجيل وحدود عباراته قبل ضبط المشاهد. تبقى المؤثرات والتعليق في مسارين منفصلين، مع الحفاظ على النطق الطبيعي ووقت قراءة الرابط وQR. لا يضيف هذا الخيار موسيقى، ولا يجعل التعليق إلزاميًا لكل فيديو.

ترخيص MIT لتعليمات مَشْهَد ولمرجع [مهارات ElevenLabs الرسمية](https://github.com/elevenlabs/skills) لا يشمل الصوت المولّد تلقائيًا؛ تتبع حقوق استخدامه [شروط الخدمة والخطة المستخدمة](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform).

## خط ثمانية

**الخط مدعوم ومستخدم في الإعلان، لكن ملفاته ليست مرفقة.** يُحمّل كل مستخدم نسخته من [ثمانية](https://font.thmanyah.com/). حقوقه لشركة ثمانية؛ يمنع [ترخيصه](https://font.thmanyah.com/licenses) إعادة توزيع ملفات الخط أو استضافتها للتنزيل. ترخيص MIT لهذا المشروع لا يشمل الخط.

وجّه `THMANYAH_FONT_DIR` إلى مجلد `thmanyahsans` المحلي أو المجلد الأب الذي يحتويه. مثال PowerShell:

```powershell
$env:THMANYAH_FONT_DIR = 'D:/Fonts/thmanyah typeface/thmanyahsans'
```

الأوزان: Regular 400، Medium 500، Bold 700، Black 900. [تفاصيل استخدام العربية والخط](skills/mashhad-video/references/arabic-and-audio.md).

## الأدوات المرفقة

| الأداة | وظيفتها |
| --- | --- |
| `inspect_environment.py` | قراءة الأدوات والتبعيات المتاحة دون تثبيت |
| `project_manifest.py` | فحص تغطية المشاهد والتداخلات والتوقيت بالإطارات |
| `media_check.py` | فك ترميز كامل، عدد إطارات دقيق، مقاس، مدة، صوت وشفافية |

السكربتات في [مجلد المهارة](skills/mashhad-video/scripts). فحص الوسائط يحتاج FFmpeg وffprobe. [مصدر الإعلان](examples/mashhad-ad) يستخدم HTML Canvas وChromium وFFmpeg، ويحتوي مولد المؤثرات الأصلي وQR المستودع. لا يضم عينات صوتية مقتبسة.

## حالة التحقق

جرت مراجعة البنية والروابط، واختبار أدوات التوقيت والوسائط، وإخراج الإعلان محليًا. رمز QR فُحص من إطارات الفيديو المصدّرة. توافق Claude Code يستند إلى صيغة Agent Skills الموثقة؛ لم يُجر اختبار جلسة داخل Claude Code. التكامل مع كل محرّك متخصص يحتاج اختبارًا في بيئته. سجل المراجعة يحدد نطاق فحص الإطارات والصوت ولا يدعي اختبارًا لم يحدث.

## الحقوق والمساهمون

**Copyright © 2026 Sultan Alfaifi.** ملفات مَشْهَد الأصلية تحت [MIT](LICENSE). أبقِ إشعار الحقوق والترخيص عند إعادة الاستخدام.

التعليمات أصلية؛ لم تُدمج أجسام مهارات خارجية أو محركاتها داخل الحزمة. نُسبت المراجع والمشاريع الخارجية وأصحابها وتراخيصها في [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) و[SOURCES.json](SOURCES.json). تراخيص تلك المشاريع والأصول مستقلة، ولا توجد شراكة أو رعاية مُدّعاة معها. المؤثرات غير الموسيقية تحتاج إثبات منشأ أو ترخيص أيضًا.

## English

Mashhad is a portable motion-design Agent Skill for **Codex and Claude Code**. It routes to a suitable renderer, coordinates frame-based media handoffs, supports Arabic typography, and separates technical checks from visual and listening review. Audio defaults to **SFX and nonmusical ambience only**. Music requires an explicit request. Optional ElevenLabs guidance uses the connected plugin when available, honors the user's selected voice, and aligns motion to the actual recording. Generated media has separate service and usage rights from the skill's MIT license.

Install from this clone with `python tools/install.py --agent both`. Invoke `$mashhad-video` in Codex or `/mashhad-video` in Claude Code. Video runtimes are separate dependencies. Thmanyah Sans is supported through a local font path and is **not redistributed**. Original project files are © 2026 Sultan Alfaifi, MIT; see the third-party notices for independent upstream rights.
