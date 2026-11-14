import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from align import words_in, hadith
m = hadith(3321, 'غفر', 'بذلك'); k = hadith(2363, 'كبد', 'اجر', back=2)
parts = []; cur = []
for w in m:
    cur.append(w)
    if w.endswith('،'): parts.append(cur); cur = []
parts.append(cur)
P = [("الدنيا تسعة وتلاتين درجة.", .73, 2.54, None), ("وفي كلب تحت البيت بينهج.", 3.44, 5.2, None), ("وحد لسه راميه بطوبة.", 5.9, 7.32, None),
     ("الناس بتضحك.", 7.86, 8.6, None), ("وواحد بيقول:", 8.96, 9.7, None), ("سمّوهم كلهم.", 9.95, 10.95, None), ("بس النبي صلى الله عليه وسلم قال:", 11.36, 13.82, None),
     (parts[0], 14.21, 19.5, "q"), (parts[1], 20.15, 22.58, "q"), (parts[2], 23.06, 24.29, "q"), (parts[3], 24.63, 26.24, "q"), (parts[4], 26.69, 28.22, "q"), (parts[5], 28.67, 30.24, "q"),
     ("وقال كمان:", 30.66, 31.46, None), (k, 31.8, 34.1, "q"), ("يعني لو شوية مية لكلب كانت سبب", 34.53, 36.43, None), ("إن ربنا يغفر لست،", 36.46, 37.98, None),
     ("تخيّل الطوبة بتعمل إيه.", 38.57, 39.92, None), ("والسم.", 40.4, 40.86, None), ("املا طبق مية.", 41.34, 42.15, None), ("وحطه برا.", 42.72, 43.22, None), ("لسه الدنيا تسعة وتلاتين.", 43.94, 45.42, None)]
open('data_dog_ar.js', 'w', encoding='utf-8').write(f'''// Egyptian Arabic dog video. Word times from pause detection on the ElevenLabs take; hadith words copied by code from fawazahmed0/hadith-api (ara-bukhari 3321, 2363).
export const DURATION = 45.7;
export const WORDS = {json.dumps(words_in(P), ensure_ascii=False)};
export const SEQ = [0,1,2,3,4,10,5,6,7,8,9];
export const CUTS = [0,5.6,7.62,11.2,14.0,20.0,28.45,30.5,34.3,41.05,43.55,45.7];
export const ROCK = 6.7;
export const PILL = "39°C";
export const PUNCH = [[1.0,.05],[6.7,.08],[9.95,.06],[28.67,.05],[33.4,.05],[38.9,.07],[40.4,.08]];
export const REFS = [{{text:"صحيح البخاري · حديث ٣٣٢١",from:11.4,to:30.4}},{{text:"صحيح البخاري · حديث ٢٣٦٣",from:30.6,to:34.25}}];
export const RTL = true; export const MAXW = 3; export const MAXC = 22;
''')
E = [("It's", .13, .34, None), ("39 degrees.", .42, 1.47, None), ("There's a dog outside your building,", 2.02, 3.42, None), ("panting.", 3.62, 4.06, None), ("Someone just threw a rock at it.", 4.69, 6.03, None),
     ("People laugh.", 6.45, 7.03, None), ("Someone says,", 7.33, 7.93, None), ("poison them all.", 8.18, 8.94, None), ("But the Prophet,", 9.38, 10.14, None), ("peace be upon him,", 10.38, 11.29, None),
     ("told us about a woman who lived a life of sin.", 11.58, 13.98, None), ("She saw a dog by a well, dying of thirst.", 14.4, 16.86, None), ("She took off her shoe,", 17.28, 18.32, None),
     ("tied it to her headscarf,", 18.48, 19.6, None), ("and pulled up water for it.", 19.8, 20.84, None), ("And Allah forgave her because of that.", 21.35, 23.34, "q"),
     ("He also said there's a reward in being kind to every living thing.", 23.86, 27.1, None), ("So if water for a dog can bring forgiveness,", 27.53, 29.82, None),
     ("think about what a rock does.", 30.03, 31.35, None), ("Or poison.", 31.66, 32.22, None), ("Fill a bowl.", 32.83, 33.33, None), ("Put it outside.", 33.85, 34.46, None), ("It's still 39 degrees.", 35.11, 36.51, None)]
open('data_dog_en.js', 'w', encoding='utf-8').write(f'''// English dog video. Word times from pause detection on the ElevenLabs take.
export const DURATION = 36.8;
export const WORDS = {json.dumps(words_in(E))};
export const SEQ = [0,1,2,3,4,10,5,6,7,8,9];
export const CUTS = [0,4.4,6.3,9.25,14.25,17.1,21.1,23.65,27.35,32.55,34.8,36.8];
export const ROCK = 5.75;
export const PILL = "39°C";
export const PUNCH = [[.5,.05],[5.75,.08],[8.2,.06],[21.4,.04],[30.9,.07],[31.7,.08],[35.6,.05]];
export const REFS = [{{text:"Sahih al-Bukhari 3321",from:9.5,to:23.4}},{{text:"Sahih al-Bukhari 2363",from:23.86,to:27.3}}];
export const RTL = false;
''')
print('data ok')
