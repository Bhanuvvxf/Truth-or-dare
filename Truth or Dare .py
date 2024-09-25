#Truth or Dare 
import time
import random
#taking the how many players in the game 

print("😍 Truth or Dare ! 😍 ")

players = []

truths = [
   "Whats something youve never told anyone before?\nనువ్వు ఎప్పుడూ ఎవరికీ చెప్పని విషయం ఏంటి?",
   "Have you ever lied to get out of trouble?\nఇబ్బందుల్లోంచి బయటపడటానికి ఎప్పుడైనా అబద్ధం చెప్పారా?",
   "What’s the strangest thing you’ve ever eaten?\nనువ్వు తిన్న వింతమైన ఆహారం ఏది?",
   "Have you ever danced in front of a mirror?\nనీ దర్పణం ముందర ఎప్పుడైనా నాట్యం చేశావా?",
   "If you could switch lives with anyone for a day, who would it be?\nఒకరోజు కోసం ఎవరిదైనా జీవితాన్ని మార్చుకోవచ్చనుకుంటే, అది ఎవరిది?",
   "What’s the most embarrassing thing you’ve done in public?\nప్రజల్లో నువ్వు చేసిన అత్యంత అవమానకరమైన పని ఏది?",
   "What’s the last thing you searched for on your phone?\nనీ ఫోన్‌లో నువ్వు చివరిగా వెతికినది ఏమిటి?",
   "If you had to be stuck on a deserted island with someone, who would it be?\nఒక అణ్వయిత్వ దీవిలో ఎవరికైనా సరే చిక్కుకుపోతే, అది ఎవరు అవుతారు?",
   "What’s the silliest fear you have?\nనీకు ఉన్న అతి మూర్ఖమైన భయం ఏంటి?",
   "Have you ever talked to yourself in the mirror?\nఎప్పుడైనా నీ దర్పణంలో నీతో మాట్లాడే ప్రయత్నం చేశావా?",
   "What’s something you’ve never told anyone before?\nనువ్వు ఎప్పుడూ ఎవరికీ చెప్పని విషయం ఏంటి?",
   "Who was your first crush?\nనీ మొదటి క్రష్ ఎవరు?",
   "What’s your biggest insecurity?\nనీకు ఉన్న అతి పెద్ద అసురక్షితత ఏమిటి?",
   "What’s the biggest lie you’ve ever told?\nనువ్వు ఎప్పుడూ చెప్పిన అతి పెద్ద అబద్ధం ఏది?",
   "What’s your most embarrassing moment?\nనీ అత్యంత అవమానకరమైన క్షణం ఏది?",
   "Have you ever had a crush on a friend’s partner?\nనీ స్నేహితుడి భాగస్వామిపై ఎప్పుడైనా క్రష్ ఉందా?",
   "What’s the most embarrassing thing your parents have caught you doing?\nనీ తల్లిదండ్రులు నిన్ను చేయడంలో పట్టుకున్న అతి అవమానకరమైన పని ఏది?",
   "What’s the meanest thing you’ve ever said to someone?\nఎప్పుడైనా ఎవరికైనా చెప్పిన అతి కష్టం మాట ఏమిటి?",
   "Have you ever broken a promise to a friend?\nఎప్పుడైనా నీ స్నేహితుడికి ఇచ్చిన హామీని ఉల్లంఘించారా?",
   "What’s the most illegal thing you’ve ever done?\nనువ్వు ఎప్పుడూ చేసిన అతి చట్ట విరుద్ధమైన పని ఏది?",
   "If you could erase one moment from your past, what would it be?\nనీ గతం నుంచి ఒక క్షణాన్ని తీసివేయాలని అనుకుంటే, అది ఏది?",
   "What’s your biggest regret in life?\nనీ జీవితంలో ఉన్న అతి పెద్ద పశ్చాత్తాపం ఏమిటి?",
   "If you could change one thing about yourself, what would it be?\nనీ గురించి ఒక విషయం మార్చుకోగలిగితే, అది ఏమిటి?",
   "What is the hardest decision you’ve ever made?\nనువ్వు ఎప్పుడూ తీసుకున్న అతి కఠినమైన నిర్ణయం ఏది?",
   "If you knew today was your last day, what would you do?\nనేడు నీ చివరి రోజు అని తెలుసుకుంటే, నువ్వు ఏమి చేస్తావు?",
   "Have you ever betrayed someone’s trust?\nఎప్పుడైనా ఎవరి నమ్మకాన్ని ధ్వంసం చేశారా?",
   "What’s the scariest thing you’ve ever done?\nనువ్వు ఎప్పుడూ చేసిన అతి భయంకరమైన పని ఏది?",
   "If you had to pick one person to be with forever, who would it be?\nఎప్పటికీ ఒక వ్యక్తితో ఉండాలి అంటే, అది ఎవరు అవుతారు?",
   "What’s the biggest risk you’ve ever taken?\nనువ్వు ఎప్పుడూ తీసుకున్న అతి పెద్ద ప్రమాదం ఏది?",
   "What’s your biggest fear in life?\nనీ జీవితంలో ఉన్న అతి పెద్ద భయం ఏమిటి?",
   "Have you ever been in love?\nఎప్పుడైనా ప్రేమలో పడిపోయారా?",
   "Who was your first kiss?\nనీ మొదటి ముద్దు ఎవరి నుంచి పొందావు?",
   "Have you ever had your heart broken?\nఎప్పుడైనా నీ హృదయం విరిగిందా?",
   "Who was your first love?\nనీ మొదటి ప్రేమ ఎవరు?",
   "What’s your worst breakup story?\nనీ అతి దురదృష్టకరమైన విరహం కథ ఏమిటి?",
   "Have you ever cheated in a relationship?\nఎప్పుడైనా సంబంధంలో నమ్మకద్రోహం చేశావా?",
   "Have you ever had a crush on a teacher?\nఎప్పుడైనా మీ ఉపాధ్యాయుడిపై క్రష్ ఉందా?",
   "Who is your current crush?\nప్రస్తుతం నీ క్రష్ ఎవరు?",
   "Have you ever been rejected by someone you liked?\nఎప్పుడైనా నువ్వు ఇష్టపడిన వ్యక్తి నిన్ను తిరస్కరించారా?",
   "What’s the most romantic thing you’ve ever done?\nనువ్వు చేసిన అతి రొమాంటిక్ పని ఏది?",
   "Who is your best friend and why?\nనీ ఉత్తమ స్నేహితుడు ఎవరు, ఎందుకు?",
   "What’s the worst thing you’ve ever said about someone behind their back?\nఎప్పుడైనా ఎవరికైనా వారి వెనుక చెప్పిన అతి చెడ్డ మాట ఏది?",
   "Have you ever lied to a friend to avoid hanging out with them?\nఎప్పుడైనా స్నేహితుడిని కలవకూడదని అబద్ధం చెప్పారా?",
   "What’s the most childish thing you’ve done recently?\nఇటీవల నువ్వు చేసిన అతి బాలపనితనం ఏది?",
   "What’s one thing you wish you could change about your friend group?\nనీ స్నేహితుల బృందంలో ఒక విషయం మార్చాలని అనుకుంటే, అది ఏమిటి?",
   "Have you ever pretended to like someone to avoid hurting their feelings?\nఎప్పుడైనా ఎవరి మనసు బాధించకుండా వారిని ఇష్టపడుతున్నట్టు నటించారా?",
   "Who is the most annoying person you know?\nనువ్వు తెలిసిన అతి కష్టమైన వ్యక్తి ఎవరు?",
   "Have you ever made fun of someone in this room?\nఈ గదిలో ఎవరికైనా నువ్వు ఎప్పుడైనా ఆటపట్టించావా?",
   "What’s the most awkward social situation you’ve ever been in?\nనువ్వు ఎదుర్కొన్న అతి విచిత్రమైన సామాజిక పరిస్థితి ఏది?",
   "Who in this room do you trust the most?\nఈ గదిలో నువ్వు ఎవరిని ఎక్కువగా నమ్ముతావు?",
   "What’s your most embarrassing nickname?\nనీ అతి అవమానకరమైన పేరు ఏమిటి?",

"Have you ever pretended to be sick to skip school?\nపాఠశాలకు వెళ్లకుండా ఉండేందుకు ఎప్పుడైనా అనారోగ్యంగా నటించారా?",

"If you had to eat one meal for the rest of your life, what would it be?\nనీ జీవితంలో మిగిలిన రోజులు కేవలం ఒకే ఒక భోజనం తినాలంటే, అది ఏది?",

"Have you ever peeked at someone else’s phone without them knowing?\nఎవరైనా తెలియకుండా వారి ఫోన్‌లో చూశారా?",

"What’s your most annoying habit?\nనీ అతి ఇబ్బందికరమైన అలవాటు ఏమిటి?",

"Have you ever laughed at a joke you didn’t understand?\nనీకు అర్థం కాని జోక్‌ను ఎప్పుడైనా నవ్వారా?",

"What’s one thing you wish you could do but can’t?\nనీకు చేయాలనిపించే కానీ చేయలేని ఒక విషయం ఏమిటి?",

"If you could change your name, what would you change it to?\nనీ పేరు మార్చుకోవాలనిపిస్తే, ఏ పేరు పెట్టుకుంటావు?",

"Have you ever sent a text to the wrong person?\nఎప్పుడైనా తప్పు వ్యక్తికి టెక్స్ట్ పంపించారా?",

"What’s the longest you’ve ever gone without a shower?\nఎన్ని రోజులు స్నానం చేయకుండా గడిపావు?",

"What’s the weirdest dream you’ve ever had?\nనీకు వచ్చిన అతి విచిత్రమైన కల ఏమిటి?",

"Have you ever eavesdropped on someone else’s conversation?\nఎప్పుడైనా ఎవరి సంభాషణను గూఢచర్యం చేసి వినారా?",

"Have you ever lied about your age?\nనీ వయస్సు గురించి ఎప్పుడైనా అబద్ధం చెప్పారా?",

"What’s one thing you do that you would never want anyone to know?\nనీ గురించి ఎవరికీ తెలియకూడని ఒక విషయం ఏమిటి?",

"Have you ever been caught cheating on a test?\nనీ ఎగ్జామ్‌లో ఎప్పుడైనా నకలు పట్టుబడారా?",

"If you could be invisible for one day, what would you do?\nఒక రోజు కనిపించకుండా ఉండాలంటే, ఏమి చేస్తావు?",

"What’s your favorite guilty pleasure?\nనీకు ఇష్టమైన గిల్టీ ప్లెజర్ ఏది?",

"What’s the dumbest thing you’ve ever said to someone?\nనీ ఇన్నాళ్లలో ఎవరికైనా చెప్పిన అతి వింత మాట ఏమిటి?",

"Have you ever lied to impress someone?\nఎవరినైనా ప్రభావితం చేయడానికి అబద్ధం చెప్పారా?",

"If you could live anywhere in the world, where would it be?\nప్రపంచంలో ఎక్కడైనా నివసించాలంటే, ఎక్కడ ఉంటావు?",

"Have you ever cried during a movie?\nసినిమా చూసేటప్పుడు ఎప్పుడైనా ఏడ్చారా?",

"What’s the worst gift you’ve ever received?\nనీకు అందిన అతి చెత్త బహుమతి ఏమిటి?",

"If you could be famous for one thing, what would it be?\nఒక విషయానికి ప్రసిద్ధిగా ఉండాలంటే, అది ఏది?",

"Have you ever Googled yourself?\nఎప్పుడైనా నిన్ను నీకే గూగుల్‌లో వెతికావా?",

"What’s the most annoying thing your family does?\nనీ కుటుంబంలో ఎవరు చేసే అతి ఇబ్బందికరమైన పని ఏమిటి?",

"Have you ever stayed up all night?\nఎప్పుడైనా రాత్రంతా నిద్రలేకుండా ఉన్నావా?",

"What’s the weirdest thing you’ve ever collected?\nనీకు కలిగిన అతి విచిత్రమైన సేకరణ ఏది?",

"Have you ever gotten caught doing something you shouldn’t have?\nనువ్వు చేయకూడని పని చేస్తూ ఎప్పుడైనా పట్టుబడ్డావా?",

"What’s the most embarrassing thing you’ve ever worn?\nనీ ధరించిన అతి అవమానకరమైన దుస్తులు ఏమిటి?",

"What’s one talent you wish you had?\nనీకు ఉండాలనిపించే ఒక ప్రతిభ ఏమిటి?",

"Have you ever fallen asleep in public?\nఎప్పుడైనా పబ్లిక్‌లో నిద్రపోయావా?",

"What’s the worst haircut you’ve ever had?\nనీకు వచ్చిన అతి చెత్త హెయిర్‌కట్ ఏది?",

"Have you ever lied about being busy?\nబిజీగా ఉన్నానని అబద్ధం చెప్పారా?",

"What’s the worst job you’ve ever had?\nనీకు లభించిన అతి చెత్త ఉద్యోగం ఏమిటి?",

"If you could be any age for a week, what age would it be?\nఒక వారం పాటు ఏ వయస్సులో అయినా ఉండాలంటే, ఏ వయస్సులో ఉండేవు?",

"Have you ever ruined someone’s surprise?\nఎవరైనా సర్ప్రైజ్‌ను ఎప్పుడైనా పాడుచేశారా?",

"What’s your favorite childhood memory?\nనీకు ఇష్టమైన బాల్య స్మృతి ఏది?",

"Have you ever been embarrassed by something you did in public?\nప్రజల్లో చేసిన పని వల్ల ఎప్పుడైనా అవమానపడటానికి కారణమయ్యావా?",

"What’s the last lie you told?\nనువ్వు చెప్పిన చివరి అబద్ధం ఏమిటి?",

"What’s one thing you’ve never told your best friend?\nనీ బాగా తెలిసిన స్నేహితుడికి ఎప్పుడూ చెప్పని విషయం ఏమిటి?",

"If you could swap lives with a celebrity, who would it be?\nఒక సెలెబ్రిటీతో నీ జీవితం మారిపోవాలంటే, అది ఎవరు?",

"What’s the most useless talent you have?\nనీకు ఉన్న అతి ఉపయోగకరమైన ప్రతిభ ఏమిటి?",

"Have you ever had a crush on a fictional character?\nఎప్పుడైనా కట్టుకథల్లోని పాత్రపై ప్రేమపడ్డారా?",

"If you could eat anything without getting fat, what would you eat?\nఎంత తిన్నా లావవకుండా ఉండాలంటే, ఏది తినేవు?",

"What’s one thing you’d never want your parents to know?\nనీ తల్లిదండ్రులు తెలుసుకోకూడని ఒక విషయం ఏమిటి?",

"What’s the most embarrassing thing you’ve ever done to impress someone?\nఎవరినైనా ప్రభావితం చేయడానికి నీ చేసిన అతి అవమానకరమైన పని ఏమిటి?",

"Have you ever re-gifted something you didn’t want?\nనీకు ఇష్టం లేని బహుమతిని ఎప్పుడైనా తిరిగి ఇచ్చారా?",

"What’s the silliest thing you’re afraid of?\nనీకు ఉన్న అతి అసమంజసమైన భయం ఏమిటి?",

"What’s the worst advice you’ve ever taken?\nనీ తీసుకున్న అతి చెత్త సలహా ఏమిటి?",

"What’s one thing you’re bad at that you wish you were good at?\nనీకు తక్కువగా వచ్చే కానీ బాగా వచ్చి ఉండాలని ఆశించే విషయం ఏమిటి?"
]


dares = [

"Dance without music for 1 minute.\nమ్యూజిక్ లేకుండా 1 నిమిషం డ్యాన్స్ చేయండి.",

"Sing your favorite song aloud.\nనీకు ఇష్టమైన పాటని జోరుగా పాడండి.",

"Do 10 jumping jacks.\n10 జంపింగ్ జాక్స్ చేయండి.",

"Let someone else send a text from your phone.\nనీ ఫోన్ నుండి ఎవరైనా ఒక మెసేజ్ పంపనివ్వండి.",

"Try to lick your elbow.\nనీ భుజాన్ని నాకడానికి ప్రయత్నించండి.",

"Wear your clothes backward for the next round.\nతరువాతి రౌండ్‌లో నీ బట్టలు వెనుక పెట్టుకోండి.",

"Speak in an accent for the next 3 rounds.\nతరువాతి 3 రౌండ్లలో వింత ఉచ్ఛారణలో మాట్లాడండి.",

"Impersonate your favorite celebrity for 1 minute.\n1 నిమిషం పాటు నీకు ఇష్టమైన సెలబ్రిటీని అనుకరించండి.",

"Let someone tickle you for 30 seconds.\nఎవరైనా 30 సెకన్ల పాటు నిన్ను గిలిగింత పెట్టనివ్వండి.",

"Try to juggle 3 random objects.\n3 యాదృచ్ఛిక వస్తువులను త్రోబల్యుతో వేగంగా తిరగడం ప్రయత్నించు.",

"Speak gibberish for the next round.\nతరువాతి రౌండ్‌లో గజిబిజి భాషలో మాట్లాడండి.",

"Do 20 push-ups.\n20 పుష్-అప్స్ చేయండి.",

"Try a handstand for 10 seconds.\n10 సెకన్ల పాటు హ్యాండ్స్టాండ్ చేయడానికి ప్రయత్నించండి.",

"Give someone a piggyback ride.\nఎవరైనా నీ భుజం మీద కూర్చోబెట్టండి.",

"Do a silly dance for 30 seconds.\n30 సెకన్ల పాటు వింతగా డ్యాన్స్ చేయండి.",

"Hop on one leg for 1 minute.\n1 నిమిషం పాటు ఒక కాలు మీద గెంతండి.",

"Balance a book on your head for 2 minutes.\n2 నిమిషాల పాటు నీ తలపై పుస్తకం ఉంచండి.",

"Walk like a crab for 1 minute.\n1 నిమిషం పాటు క్రాబ్ లాగా నడవండి.",

"Act like a robot for the next 2 minutes.\nతరువాతి 2 నిమిషాల పాటు రోబోట్ లాగా నటించండి.",

"Speak in rhyme for the next 3 rounds.\nతరువాతి 3 రౌండ్లలో పద్యంలో మాట్లాడండి.",

"Eat a spoonful of mustard.\nమస్టర్డ్‌ యొక్క ఒక చెంచా తినండి.",

"Do the worm dance across the room.\nగదిలో వరం డ్యాన్స్ చేయండి.",

"Let someone blindfold you and feed you something.\nఎవరైనా నీ కళ్ళకు గంతు కట్టి నీకు ఏదైనా తినిపించనివ్వండి.",

"Post an embarrassing photo on social media.\nసోషల్ మీడియాలో ఒక అవమానకరమైన ఫోటోను పోస్ట్ చేయండి.",

"Draw something on your face with a marker.\nమార్కర్‌తో నీ ముఖంపై ఏదైనా గీయండి.",

"Wear socks on your hands for the next 5 minutes.\nతరువాతి 5 నిమిషాల పాటు నీ చేతులకు సాక్స్ ధరించండి.",

"Take a silly selfie and send it to someone random.\nవింత సెల్ఫీ తీసుకుని యాదృచ్ఛికంగా ఎవరికైనా పంపండి.",

"Try to balance a spoon on your nose.\nనీ ముక్కుపై చెంచా సమతుల్యంగా ఉంచి చూడండి.",

"Do 15 squats.\n15 స్క్వాట్స్ చేయండి.",

"Pretend you're an animal for 1 minute.\n1 నిమిషం పాటు జంతువులా నటించండి.",

"Speak in whispers for the next 2 rounds.\nతరువాతి 2 రౌండ్లలో గుసగుసలలో మాట్లాడండి.",

"Spin around 10 times and try to walk in a straight line.\n10 సార్లు తిరిగి నేరుగా నడవడానికి ప్రయత్నించండి.",

"Pretend to be a waiter and take snack orders.\nవెయిటర్‌లా నటించి స్నాక్స్ ఆర్డర్లు తీసుకోండి.",

"Do a funny face for 1 minute.\n1 నిమిషం పాటు వింత ముఖం చేయండి.",

"Make animal sounds for the next 3 minutes.\nతరువాతి 3 నిమిషాల పాటు జంతువుల శబ్దాలు చేయండి.",

"Wear a blindfold for the next round.\nతరువాతి రౌండ్‌లో గంతు కట్టి ఉండు.",

"Imitate someone in the group.\nగ్రూప్‌లో ఎవరో ఒకరిని అనుకరించండి.",

"Talk without using your tongue.\nనీ నాలుకను ఉపయోగించకుండా మాట్లాడండి.",

"Hold your breath for 20 seconds.\n20 సెకన్ల పాటు నీ శ్వాసను నిలిపి ఉంచండి.",

"Do your best dance move.\nనీ అత్యుత్తమ డ్యాన్స్ మూమెంట్ చేయండి.",

"Let the group rename you for the rest of the game.\nగ్రూప్ నీకు ఈ గేమ్ మొత్తం కొత్త పేరు పెట్టనివ్వండి.",

"Put an ice cube in your mouth until it melts.\nనీ నోట్లో ఐస్ క్యూబ్ ఉంచి అది కరగేవరకు ఉంచండి.",

"Act like your favorite superhero for 1 minute.\nనీకు ఇష్టమైన సూపర్ హీరోలా 1 నిమిషం పాటు నటించండి.",

"Do 10 burpees.\n10 బర్పీస్ చేయండి.",

"Speak in a high-pitched voice for the next 3 rounds.\nతరువాతి 3 రౌండ్లలో పైన ఉన్న స్వరంలో మాట్లాడండి.",

"Let someone redo your hairstyle.\nఎవరైనా నీ హెయిర్ స్టైల్ మార్చనివ్వండి.",

"Talk only using hand gestures for 2 minutes.\n2 నిమిషాల పాటు చేతి సంకేతాల ద్వారా మాత్రమే మాట్లాడండి.",

"Eat something without using your hands.\nనీ చేతులను ఉపయోగించకుండా ఏదైనా తినండి.",

"Imitate a celebrity's iconic scene for 1 minute.\n1 నిమిషం పాటు ఒక సెలబ్రిటీ యొక్క ప్రసిద్ధ సన్నివేశాన్ని అనుకరించండి.",

"Try to walk backward for 1 minute.\n1 నిమిషం పాటు వెనుకకు నడవడానికి ప్రయత్నించండి.",

"Do your best animal impression.\nనీకు ఇష్టమైన జంతువు యొక్క ఉత్తమ అనుకరణ చేయండి.",

"Let someone draw on your face with a washable marker.\nఎవరైనా నీ ముఖంపై వాషబుల్ మార్కర్‌తో గీయనివ్వండి.",

"Speak only in questions for the next 5 minutes.\nతరువాతి 5 నిమిషాల పాటు ప్రశ్నల రూపంలో మాత్రమే మాట్లాడండి.",

"Do 10 sit-ups.\n10 సిట్-అప్స్ చేయండి.",

"Wear shoes on your hands for the next round.\nతరువాతి రౌండ్‌లో నీ చేతులకు బూట్లు ధరించండి.",

"Let someone fix your hair however they want.\nఎవరైనా నీ హెయిర్‌ను వాళ్లు ఇష్టమొచ్చినట్టు సర్దుకోవడానికి అనుమతించండి.",

"Sing everything you say for the next 3 rounds.\nతరువాతి 3 రౌండ్లలో మాట్లాడే ప్రతిదాన్ని పాడి చెప్పండి.",

"Hold a plank for 1 minute.\n1 నిమిషం పాటు ప్లాంక్‌లో ఉండు.",

"Pretend you're a baby for 2 minutes.\n2 నిమిషాల పాటు బిడ్డలా నటించండి.",

"Do your best evil laugh for 30 seconds.\n30 సెకన్ల పాటు నీ అత్యుత్తమ దుష్ట నవ్వు చేయండి.",

"Wear a hat made out of something in the room.\nగదిలోని ఏదైనా ఉపయోగించి ఒక టోపీ ధరించండి.",

"Try to do a cartwheel.\nకార్ట్‌వీల్ చేయడానికి ప్రయత్నించండి.",

"Let someone paint your nails.\nఎవరైనా నీ గోర్లకు రంగు వేసినట్టు అనుమతించండి.",

"Wear sunglasses for the next 3 rounds.\nతరువాతి 3 రౌండ్లలో సన్‌గ్లాసెస్ ధరించండి.",

"Do your best impression of someone else in the group.\nగ్రూప్‌లోని మరో వ్యక్తిని అనుకరించడానికి ప్రయత్నించండి.",

"Put a random object on your head and balance it for 1 minute.\nయాదృచ్ఛికంగా ఒక వస్తువును నీ తలపై ఉంచి 1 నిమిషం పాటు సమతుల్యంగా ఉంచండి.",

"Pretend you're a waiter and take everyone's order.\nవెయిటర్‌లా నటించి అందరి ఆర్డర్ తీసుకోండి.",

"Spin in a circle 15 times and try to walk straight.\n15 సార్లు చుట్టూ తిరిగి నేరుగా నడవడానికి ప్రయత్నించండి.",

"Pretend you're stuck in a box for 2 minutes.\n2 నిమిషాల పాటు బాక్స్‌లో ఇరుక్కుపోయినట్టు నటించండి.",

"Do the chicken dance for 1 minute.\n1 నిమిషం పాటు చికెన్ డ్యాన్స్ చేయండి.",

"Make the most ridiculous face you can and hold it for 30 seconds.\n30 సెకన్ల పాటు అతి విచిత్రమైన ముఖాన్ని చేసి ఉంచండి.",

"Do 5 cartwheels in a row.\nసరాసరి 5 కార్ట్‌వీల్‌లు చేయండి.",

"Wear your socks on your hands for the next 2 rounds.\nతరువాతి 2 రౌండ్లలో నీ చేతులకు సాక్స్ ధరించండి.",

"Let someone put a mystery food in your mouth while blindfolded.\nనువ్వు కళ్ళకు గంతు కట్టుకుని ఉంటే ఎవరైనా నీకు మిస్టరీ ఫుడ్ పెట్టనివ్వండి.",

"Walk around like a robot for 1 minute.\n1 నిమిషం పాటు రోబోట్లా నడవండి.",

"Let someone redo your outfit.\nఎవరైనా నీ దుస్తులను మార్చుకోనివ్వండి.",

"Hold your breath and try to sing a song.\nనీ శ్వాసను నిలిపి ఒక పాట పాడడానికి ప్రయత్నించండి.",

"Do the moonwalk for 30 seconds.\n30 సెకన్ల పాటు మూన్‌వాక్ చేయండి.",

"Imitate a famous singer for 1 minute.\n1 నిమిషం పాటు ఒక ప్రసిద్ధ గాయకుడిని అనుకరించండి.",

"Pretend to be a cat for 2 minutes.\n2 నిమిషాల పాటు పిల్లిలాగా నటించండి.",

"Wear your shoes on the wrong feet for the next round.\nతరువాతి రౌండ్‌లో నీ బూట్లు తికమకగా ధరించండి.",

"Try to talk without opening your mouth.\nనీ నోటిని తెరవకుండా మాట్లాడడానికి ప్రయత్నించండి.",

"Let someone draw a mustache on your face.\nఎవరైనా నీ ముఖంపై మీసాలు గీయనివ్వండి.",

"Hold an ice cube in your hand until it melts.\nనీ చేతిలో ఐస్ క్యూబ్ కరిగిపోయే వరకు ఉంచండి.",

"Do 20 jumping jacks in slow motion.\nస్లో మోషన్‌లో 20 జంపింగ్ జాక్స్ చేయండి.",

"Sing the alphabet backward.\nఅక్షరమాలని వెనుకకు పాడండి.",

"Pretend to be a pirate for the next 2 minutes.\nతరువాతి 2 నిమిషాల పాటు కస్టోడియన్‌లా నటించండి.",

"Let someone mess up your hair.\nఎవరైనా నీ హెయిర్‌ను చెడగొట్టనివ్వండి.",

"Pretend you are swimming on the floor for 1 minute.\n1 నిమిషం పాటు నేలపై ఈత కొడుతున్నట్టు నటించండి.",

"Act like you’re in slow motion for 2 minutes.\n2 నిమిషాల పాటు స్లో మోషన్‌లో ఉన్నట్టు నటించండి.",

"Let someone else put makeup on you.\nఎవరైనా నీకు మేకప్ పెట్టనివ్వండి.",

"Try to do a handstand against a wall.\nగోడపై హ్యాండ్స్టాండ్ చేయడానికి ప్రయత్నించండి.",

"Mimic an animal sound for 1 minute.\n1 నిమిషం పాటు జంతువు శబ్దం అనుకరించండి.",

"Let someone tape something to your face.\nఎవరైనా నీ ముఖానికి ఏదైనా టేప్ చేయనివ్వండి.",

"Pretend to eat like a dinosaur for 2 minutes.\n2 నిమిషాల పాటు డైనోసార్‌లా తినడానికి ప్రయత్నించండి.",

"Do 5 cartwheels, even if you don’t know how.\nనీకు తెలియకపోయినా 5 కార్ట్‌వీల్‌లు చేయండి.",

"Jump up and down as high as you can for 30 seconds.\n30 సెకన్ల పాటు ఎంత ఎత్తుకు అయితే అంత ఎత్తుగా ఎగరండి.",

"Let someone create a hairstyle for you.\nఎవరైనా నీ కోసం ఒక హెయిర్‌స్టైల్ చేయనివ్వండి.",

"Try to keep a straight face while someone tries to make you laugh.\nఎవరైనా నిన్ను నవ్వించడానికి ప్రయత్నిస్తున్నప్పుడు నీ ముఖాన్ని నేరుగా ఉంచండి.",

"Hold a funny pose for 1 minute.\n1 నిమిషం పాటు వింతగా నిలబడి ఉండు."




]


def Start_game():
   try:
       global number_of_players
       number_of_players = int(input("Enter how many players are playing Truth or Dare game : "))
   except ValueError:
    print("Enter players only number")


   if number_of_players < 3 :
      print("Gather a group of friends (at least 3 players).")
      Start_game()

Start_game()
    
    

for i in range(number_of_players):
    try:
      players_name = input(f"Enter the player{i+1} name : ")
      players.append(players_name)
    except ValueError:
       print("Enter only names ")


print("Players list : ",players)

def countdown_timer(minutes=0, seconds=10):
    total_seconds = minutes * 60 + seconds  # Convert total time to seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)  # Calculate minutes and seconds
        timer = '{:02d}'.format(secs)  # Format time as MM:SS
        print(timer, end='\r')  # Print the timer on the same line
        time.sleep(1)  # Wait for 1 second
        total_seconds -= 1  # Decrease the total seconds by 1
    r = random.randint(0,number_of_players-1)
    k = random.randint(0,len(truths))
    s = random.randint(0,len(dares))
    if len(truths) == 0:
       print("game comepleted successfully !")
    if len(dares) == 0 :
       print("game completed successfully !")
    print(players[r])
    ask = input("Truth or Dare ! (T,D) : ")
    if ask == "T":
       
       t = truths.pop(k)
       print("*"*149)
       print(t)
       print("*"*149)
       print("They answer a personal question honestly.")
       c = input("Task completed Yes or No (Y/N): ")
       if c == "Y":
          countdown_timer()
          
       elif c == "N":
          reason = input("Enter the reason : ")
          print(reason)
          print("Continue the game .")
          countdown_timer()
          
       else:
          print("Enter valid only Y or N ")
          countdown_timer()
    elif ask == "D":
       d = dares.pop(s)
       print("*"*149)
       print(d)
       print("*"*149)
       print("They complete a challenging or fun task.")
       c = input("Task completed Yes or No (Y/N): ")
       if c == "Y":
          countdown_timer()
          
       elif c == "N":
          reason = input("Enter the reason : ")
          print(reason)
          print("Continue the game .")
          countdown_timer()
          
       else:
          print("Enter valid only Y or N ")
          countdown_timer()
    else:
       print("Enter valid value T or D ")
       countdown_timer()

    



countdown_timer()