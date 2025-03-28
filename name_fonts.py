import logging

logger = logging.getLogger(__name__)

# Font styles specifically for names
NORMAL_FONTS = {
    "Simple Star": "★ NAME ★",
    "Simple Heart": "♡ NAME ♡",
    "Simple Crown": "👑 NAME",
    "Simple Magic": "✨ NAME",
    "Simple Rose": "🌹 NAME",
    "Simple Diamond": "💎 NAME",
    "Simple Flower": "❀ NAME",
    "Simple Fire": "🔥 NAME",
    "Simple Ice": "❄️ NAME",
    "Simple Rainbow": "🌈 NAME",
    "Simple Cloud": "☁️ NAME",
    "Simple Moon": "🌙 NAME",
    "Simple Sun": "☀️ NAME",
    "Simple Star": "⭐ NAME",
    "Simple Heart": "💖 NAME",
    "Simple Crown": "👑 NAME",
    "Simple Butterfly": "🦋 NAME",
    "Simple Lotus": "🪷 NAME",
    "Simple Galaxy": "🌌 NAME",
    "Simple Unicorn": "🦄 NAME",
    "Simple Angel": "👼 NAME",
    "Simple Crystal": "💫 NAME",
    "Simple Leaf": "🍃 NAME",
    "Simple Music": "🎵 NAME",
    "Simple Sparkle": "✧ NAME ✧",
    "Simple Clover": "🍀 NAME",
    "Simple Pearl": "🫧 NAME",
    "Simple Dove": "🕊️ NAME",
    "Simple Ribbon": "🎀 NAME",
    "Simple Feather": "🪽 NAME",
    "Simple Candy": "🍬 NAME",
    "Simple Gem": "💝 NAME",
    "Simple Fairy": "🧚 NAME",
    "Simple Wings": "🪽 NAME 🪽",
    "Simple Glow": "⟡ NAME ⟡"
}

FANCY_FONTS = {
    "Butterfly Magic": "➺꯭ ꯭𝅥‌꯭𝆬‌🦋⃪꯭ NAME ─‌⃛┼ 𝞄⃕𝖋𝖋 .🥵⃝⃝ᬽ꯭ ⃪꯭ ꯭��‌꯭𝆬‌➺꯭⎯⎯᪵᪳",
    "Heart Crystal": "🤍 ⍣⃪‌ NAME ‌ᵃᵐ⛦⃕‌.❛𝆺𝅥⤹࿗𓆪ꪾ™",
    "Fire Dragon": "ᯓ𓆰𝅃🔥.⃪⍣꯭꯭NAME𓆪꯭🝐",
    "Star Shine": "➺ ‌⃪⃜ NAME ✦ 𝆺𝅥⎯ꨄ",
    "Love Heart": "❛ .𝁘ໍ. NAME 𓆪ִֶָ ֺ⎯꯭‌ 𓆩💗𓆪𓈒",
    "Panda Style": "𓆰𝅃꯭᳚𓄂️𝆺𝅥⃝🔥 NAME ‌⃪‌ ᷟ𓆩 . 乛|⁪⁬⁮⁮⁮⁮ ‌⁪⁬𓆪🐼™",
    "Lion Power": "ᯓ𓆰𝅃꯭᳚🦁NAME.˶‌‌꯭꯭꯭꯭꯭꯭֟፝ ⚡꯭꯭꯭꯭꯭",
    "Peacock Royal": "◄❥‌‌❥ ⃝⃪⃕🦚NAME⟵᷽᷍.˚‌‌‌‌◡‌⃝🐬᪳ ‌⃪𔘓❁‌‌❍•:➛",
    "OP Style": "ᯓ𓆰 𝅃.™ NAME ٭ - 𓆪ꪾ⌯ 🜲 ˹ 𝐎ᴘ ˼",
    "X Style": "—‌‌ 𝐈тᷟʑ‌꯭𓄂︪︫︠𓆩〭〬NAME.⍣⃪‌ ꭗ‌‌𝆺꯭𝅥𔘓༌🪽⎯꯭‌⎯꯭ ꯭",
    "Butterfly Dream": "⋆❀NAME❀⋆",
    "Fire Heart": "𓆰⎯꯭꯭֯‌⌯ NAME.𓂃ֶꪳ 𓆩〭〬🔥𓆪ꪾ",
    "White Heart": "🍹𝆺𝅥⃝🤍 NAME ‌⃪‌ ᷟ●.🤍᪳𝆺꯭𝅥⎯꯭‌⎯꯭",
    "Butterfly Crown": "⋆⎯፝֟፝֟⎯᪵ NAME 𝆺꯭𝅥. ᭄꯭🦋꯭᪳᪳᪻⎯‌⎯🐣",
    "Fire X": "⟶‌ꭙ⋆🔥𓆩〬 NAME .⎯᳝֟፝֟⎯‌ꭙ⋆🔥",
    "White X": "⟶‌ꭙ⋆🤍𓆩〬 NAME .🤍᪳𝆺꯭𝅥⎯᳝֟፝֟⎯‌",
    "Crown Flower": "⋆─፝─᪵།‌꯭. NAME ا۬‌𝆺𝅥⃝🌸𝄄꯭꯭𝄄꯭꯭ 𝅥‌꯭𝆬‌👑",
    "Butterfly Heart": "❛ .𝁘ໍ. NAME ꨄ 🦋𓂃•",
    "Swan Style": "⟶‌𓆩〬𝁘ໍ.NAME𓂃˖ॐ🪼⎯᳝֟፝⎯‌ꭙ⋆",
    "Fire Star": "★彡 NAME 彡★",
    "Crystal Magic": "꧁༺ NAME ༻꧂",
    "Royal Crown": "👑NAME👑",
    "Dragon Fire": "†† NAME ††",
    "Star Magic": "✩⋆｡˚NAME˚｡⋆✩",
    "Angel Wings": "⊱✿NAME✿⊰",
    "Diamond Shine": "💎〽️ NAME 〽️💎",
    "Phoenix Fire": "🔥⊱ NAME ⊰🔥",
    "Rainbow Magic": "⋆⭒˚｡⋆ NAME ⋆｡˚⭒⋆",
    "Crystal Heart": "❀.(*´◡`*)NAME(*´◡`*).❀",
    "Royal Guard": "⚔️ NAME ⚔️",
    "Moon Light": "☽ NAME ☾",
    "Star Dust": "✧⋄ NAME ⋄✧",
    "Ocean Wave": "≋≋ NAME ≋≋",
    "Thunder Strike": "⚡ NAME ⚡",
    "Magic Spell": "✤✥ NAME ✥✤",
    "Dragon Scale": "༺❀ NAME ❀༻",
    "Crystal Ball": "┊⊱ NAME ⊰┊",
    "Angel Halo": "☯ NAME ☯",
    "Mystic Heart": "🤍 ⍣⃪‌ NAME ‌ᵃᵐ⛦⃕‌.❛𝆺𝅥⤹࿗𓆪ꪾ™",
    "Love Sparkle": "ღ NAME ღ",
    "Moon Flower": "𓂃❛ NAME ⟶‌. ❜ 🌙⤹🌸",
    "Music Style": "❍⏤‌‌NAME●.●───♫▷",
    "Fire Star": "★彡[NAME]彡★",
    "Dragon Style": "꧁༺NAME༻꧂",
    "Crystal Heart": "❀.(*´◡`*)NAME(*´◡`*).❀",
    "Star Magic": "✩⋆｡˚NAME˚｡⋆✩",
    "Angel Wings": "⊱✿NAME✿⊰",
    "Royal Crown": "👑NAME👑",
    "Love Sparkle": "ღ NAME ღ",
    "Butterfly Dream": "⋆❀NAME❀⋆",
    "Galaxy Star": "★彡 NAME 彡★",
    "Rainbow Heart": "♥︎NAME♥︎",
    "Mystic Heart": "🤍 ⍣⃪‌ NAME ‌ᵃᵐ⛦⃕‌.❛𝆺𝅥⤹࿗𓆪ꪾ™",
    "Fire Dragon": "ᯓ𓆰𝅃🔥.⃪⍣꯭꯭NAME𓆪꯭🝐",
    "Star Light": "➺ ‌⃪⃜ NAME ✦ 𝆺𝅥⎯ꨄ",
    "Love Crystal": "❛ NAME.𝁘ໍ.𓆪ִֶָ ֺ⎯꯭‌ 𓆩💗𓆪𓈒",
    "Panda Style": "𓆰𝅃꯭᳚𓄂️𝆺𝅥⃝🔥 NAME ‌⃪‌ ᷟ𓆩 . 乛|⁪⁬⁮⁮⁮⁮ ‌⁪⁬𓆪🐼™",
    "Lion King": "ᯓ𓆰𝅃꯭᳚🦁NAME.˶‌‌꯭꯭꯭꯭꯭꯭֟፝ ⚡꯭꯭꯭꯭꯭",
    "Ocean Dream": "◄❥‌‌❥ ⃝⃪⃕🦚NAME⟵᷽᷍.˚‌‌‌‌◡‌⃝🐬᪳ ‌⃪𔘓❁‌‌❍•:➛",
    "Butterfly Magic": "➺꯭ ꯭𝅥‌꯭𝆬‌🦋⃪꯭ NAME ─‌⃛┼ 𝞄⃕𝖋𝖋 .🥵⃝⃝ᬽ꯭ ⃪꯭ ꯭𝅥‌꯭𝆬‌➺꯭⎯⎯᪵᪳",
    "OP Style": "ᯓ𓆰 𝅃.™ NAME ٭ - 𓆪ꪾ⌯ 🜲 ˹ 𝐎ᴘ ˼",
    "X Style": "—‌‌ 𝐈тᷟʑ‌꯭𓄂︪︫︠𓆩〭〬NAME.⍣⃪‌ ꭗ‌‌𝆺꯭𝅥𔘓༌🪽⎯꯭‌⎯꯭ ꯭",
    "Butterfly Love": "𓆰𓏲.𓂃ֶꪳ 𓆩〭〬NAME🦋𓆪ꪾ",
    "Fire Heart": "𓆰⎯꯭꯭֯‌⌯ NAME.𓂃ֶꪳ 𓆩〭〬🔥𓆪ꪾ",
    "Heart Crown": "🍹𝆺𝅥⃝🤍 NAME ‌⃪‌ ᷟ●.🤍᪳𝆺꯭𝅥⎯꯭‌⎯꯭",
    "Baby Bird": "⋆⎯፝֟፝֟⎯᪵ NAME 𝆺꯭𝅥. ᭄꯭🦋꯭᪳᪳᪻⎯‌⎯🐣",
    "Fire Line": "⟶‌ꭙ⋆🔥𓆩〬 NAME .⎯᳝֟፝֟⎯‌ꭙ⋆🔥",
    "Heart Line": "⟶‌ꭙ⋆🔥𓆩〬 NAME .🤍᪳𝆺꯭𝅥⎯᳝֟፝֟⎯‌",
    "Crown Flower": "⋆─፝─᪵།‌꯭. NAME ا۬‌𝆺𝅥⃝🌸𝄄꯭꯭𝄄꯭꯭ 𝅥‌꯭𝆬‌👑",
    "Butterfly Simple": "❛ NAME .𝁘ໍ.ꨄ 🦋𓂃•",
    "Swan Style": "⟶‌𓆩〬𝁘ໍ.NAME𓂃˖ॐ🪼⎯᳝֟፝⎯‌ꭙ⋆",
    "Fire Simple": "⏤‌‌ NAME.𓂃 🔥𝆺𝅥 🜲 ⌯",
    "Fire Heart Pro": "𓆰⎯꯭꯭֯‌.𓂃ֶꪳ NAME 𓆩〭〬🔥𓆪ꪾ",
    "Bow Style": ".𝁘ໍ⎯꯭‌- NAME .⌯ 𝘅𝗗 𓂃⎯꯭‌ ִֶָ ֺ🎀",
    "Moon Flower": "𓂃❛ NAME ⟶‌. ❜ 🌙⤹🌸",
    "Music Style": "❍⏤‌‌NAME●.●───♫▷"
}

# Character mappings for different font styles
STYLE_MAPS = {
    "Circle Style": {
        'A': 'Ⓐ', 'B': 'Ⓑ', 'C': 'Ⓒ', 'D': 'Ⓓ', 'E': 'Ⓔ', 'F': 'Ⓕ', 'G': 'Ⓖ', 'H': 'Ⓗ', 'I': 'Ⓘ', 'J': 'Ⓙ',
        'K': 'Ⓚ', 'L': 'Ⓛ', 'M': 'Ⓜ', 'N': 'Ⓝ', 'O': 'Ⓞ', 'P': 'Ⓟ', 'Q': 'Ⓠ', 'R': 'Ⓡ', 'S': 'Ⓢ', 'T': 'Ⓣ',
        'U': 'Ⓤ', 'V': 'Ⓥ', 'W': 'Ⓦ', 'X': 'Ⓧ', 'Y': 'Ⓨ', 'Z': 'Ⓩ'
    },
    "Square Style": {
        'A': '🄰', 'B': '🄱', 'C': '🄲', 'D': '🄳', 'E': '🄴', 'F': '🄵', 'G': '🄶', 'H': '🄷', 'I': '🄸', 'J': '🄹',
        'K': '🄺', 'L': '🄻', 'M': '🄼', 'N': '🄽', 'O': '🄾', 'P': '🄿', 'Q': '🅀', 'R': '🅁', 'S': '🅂', 'T': '🅃',
        'U': '🅄', 'V': '🅅', 'W': '🅆', 'X': '🅇', 'Y': '🅈', 'Z': '🅉'
    },
    "Bold Style": {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'I': '𝐈', 'J': '𝐉',
        'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍', 'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓',
        'U': '𝐔', 'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙'
    },
    "Math Bold": {
        'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛', 'I': '𝗜', 'J': '𝗝',
        'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥', 'S': '𝗦', 'T': '𝗧',
        'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭'
    },
    "Monospace": {
        'A': '𝙰', 'B': '𝙱', 'C': '𝙲', 'D': '𝙳', 'E': '𝙴', 'F': '𝙵', 'G': '𝙶', 'H': '𝙷', 'I': '𝙸', 'J': '𝙹',
        'K': '𝙺', 'L': '𝙻', 'M': '𝙼', 'N': '𝙽', 'O': '𝙾', 'P': '𝙿', 'Q': '𝚀', 'R': '𝚁', 'S': '𝚂', 'T': '𝚃',
        'U': '𝚄', 'V': '𝚅', 'W': '𝚆', 'X': '𝚇', 'Y': '𝚈', 'Z': '𝚉'
    },
    "Ancient Style": {
        'A': 'Ꭺ', 'B': 'Ᏼ', 'C': 'Ꮯ', 'D': 'Ꭰ', 'E': 'Ꭼ', 'F': 'Ꮀ', 'G': 'Ꮐ', 'H': 'Ꮋ', 'I': 'Ꮖ', 'J': 'Ꮰ',
        'K': 'Ꮶ', 'L': 'Ꮮ', 'M': 'Ꮇ', 'N': 'Ν', 'O': 'Ꮎ', 'P': 'Ꮲ', 'Q': 'Ꭴ', 'R': 'Ꭱ', 'S': 'Ꮪ', 'T': 'Ꭲ',
        'U': 'Ꮜ', 'V': 'Ꮩ', 'W': 'Ꮃ', 'X': 'Ꮭ', 'Y': 'Ꮍ', 'Z': 'Ꮓ'
    },
    "Medieval Style": {
        'A': 'ᗩ', 'B': 'ᗷ', 'C': 'ᑕ', 'D': 'ᗪ', 'E': 'E', 'F': 'ᖴ', 'G': 'G', 'H': 'ᕼ', 'I': 'I', 'J': 'ᒍ',
        'K': 'K', 'L': 'ᒪ', 'M': 'ᗰ', 'N': 'ᑎ', 'O': 'O', 'P': 'ᑭ', 'Q': 'ᑫ', 'R': 'ᖇ', 'S': 'ᔕ', 'T': 'T',
        'U': 'ᑌ', 'V': 'ᐯ', 'W': 'ᗯ', 'X': '᙭', 'Y': 'Y', 'Z': 'ᘔ'
    },
    "Cursive Style": {
        'A': '𝓐', 'B': '𝓑', 'C': '𝓒', 'D': '𝓓', 'E': '𝓔', 'F': '𝓕', 'G': '𝓖', 'H': '𝓗', 'I': '𝓘', 'J': '𝓙',
        'K': '𝓚', 'L': '𝓛', 'M': '𝓜', 'N': '𝓝', 'O': '𝓞', 'P': '𝓟', 'Q': '𝓠', 'R': '𝓡', 'S': '𝓢', 'T': '𝓣',
        'U': '𝓤', 'V': '𝓥', 'W': '𝓦', 'X': '𝓧', 'Y': '𝓨', 'Z': '𝓩'
    },
    "Double Struck": {
        'A': '𝔸', 'B': '𝔹', 'C': 'ℂ', 'D': '𝔻', 'E': '𝔼', 'F': '𝔽', 'G': '𝔾', 'H': 'ℍ', 'I': '𝕀', 'J': '𝕁',
        'K': '𝕂', 'L': '𝕃', 'M': '𝕄', 'N': 'ℕ', 'O': '𝕆', 'P': 'ℙ', 'Q': 'ℚ', 'R': 'ℝ', 'S': '𝕊', 'T': '𝕋',
        'U': '𝕌', 'V': '𝕍', 'W': '𝕎', 'X': '𝕏', 'Y': '𝕐', 'Z': 'ℤ'
    },
    "Asian Style": {
        'A': '卂', 'B': '乃', 'C': '匚', 'D': '刀', 'E': '乇', 'F': '下', 'G': '厶', 'H': '卄', 'I': '工', 'J': '丁',
        'K': '长', 'L': '乚', 'M': '从', 'N': '𠘨', 'O': '口', 'P': '尸', 'Q': '㔿', 'R': '尺', 'S': '丂', 'T': '丅',
        'U': '凵', 'V': 'リ', 'W': '山', 'X': '乂', 'Y': '丫', 'Z': '乙'
    },
    "Runic Style": {
        'A': 'ᚨ', 'B': 'ᛒ', 'C': 'ᚲ', 'D': 'ᛞ', 'E': 'ᛖ', 'F': 'ᚠ', 'G': 'ᚷ', 'H': 'ᚺ', 'I': 'ᛁ', 'J': 'ᛃ',
        'K': 'ᚲ', 'L': 'ᛚ', 'M': 'ᛗ', 'N': 'ᚾ', 'O': 'ᛟ', 'P': 'ᛈ', 'Q': 'ᛩ', 'R': 'ᚱ', 'S': 'ᛋ', 'T': 'ᛏ',
        'U': 'ᚢ', 'V': 'ᚡ', 'W': 'ᚹ', 'X': 'ᛪ', 'Y': 'ᚤ', 'Z': 'ᛉ'
    },
    "Ethiopic Style": {
        'A': 'ል', 'B': 'ጌ', 'C': 'ር', 'D': 'ዕ', 'E': 'ቿ', 'F': 'ቻ', 'G': 'ኗ', 'H': 'ዘ', 'I': 'ጎ', 'J': 'ጋ',
        'K': 'ጕ', 'L': 'ረ', 'M': 'ጠ', 'N': 'ክ', 'O': 'ዐ', 'P': 'የ', 'Q': 'ዒ', 'R': 'ዪ', 'S': 'ነ', 'T': 'ፕ',
        'U': 'ሁ', 'V': 'ሀ', 'W': 'ሠ', 'X': 'ሸ', 'Y': 'ሃ', 'Z': 'ጊ'
    },
    "Bubble Style": {
        'A': 'ⓐ', 'B': 'ⓑ', 'C': 'ⓒ', 'D': 'ⓓ', 'E': 'ⓔ', 'F': 'ⓕ', 'G': 'ⓖ', 'H': 'ⓗ', 'I': 'ⓘ', 'J': 'ⓙ',
        'K': 'ⓚ', 'L': 'ⓛ', 'M': 'ⓜ', 'N': 'ⓝ', 'O': 'ⓞ', 'P': 'ⓟ', 'Q': 'ⓠ', 'R': 'ⓡ', 'S': 'ⓢ', 'T': 'ⓣ',
        'U': 'ⓤ', 'V': 'ⓥ', 'W': 'ⓦ', 'X': 'ⓧ', 'Y': 'ⓨ', 'Z': 'ⓩ'
    },
    "Small Caps": {
        'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ꜰ', 'G': 'ɢ', 'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ',
        'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ', 'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ',
        'U': 'ᴜ', 'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ'
    },
    "Script Style": {
        'A': '𝒜', 'B': 'ℬ', 'C': '𝒞', 'D': '𝒟', 'E': 'ℰ', 'F': 'ℱ', 'G': '𝒢', 'H': 'ℋ', 'I': 'ℐ', 'J': '𝒥',
        'K': '𝒦', 'L': 'ℒ', 'M': 'ℳ', 'N': '𝒩', 'O': '𝒪', 'P': '𝒫', 'Q': '𝒬', 'R': 'ℛ', 'S': '𝒮', 'T': '𝒯',
        'U': '𝒰', 'V': '𝒱', 'W': '𝒲', 'X': '𝒳', 'Y': '𝒴', 'Z': '𝒵'
    },
    "Fraktur Style": {
        'A': '𝔄', 'B': '𝔅', 'C': 'ℭ', 'D': '𝔇', 'E': '𝔈', 'F': '𝔉', 'G': '𝔊', 'H': 'ℌ', 'I': 'ℑ', 'J': '𝔍',
        'K': '𝔎', 'L': '𝔏', 'M': '𝔐', 'N': '𝔑', 'O': '𝔒', 'P': '𝔓', 'Q': '𝔔', 'R': 'ℜ', 'S': '𝔖', 'T': '𝔗',
        'U': '𝔘', 'V': '𝔙', 'W': '𝔚', 'X': '𝔛', 'Y': '𝔜', 'Z': 'ℨ'
    },
    "Serif Bold": {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'I': '𝐈', 'J': '𝐉',
        'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍', 'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓',
        'U': '𝐔', 'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙'
    },
    "Sans Serif": {
        'A': '𝖠', 'B': '𝖡', 'C': '𝖢', 'D': '𝖣', 'E': '𝖤', 'F': '𝖥', 'G': '𝖦', 'H': '𝖧', 'I': '𝖨', 'J': '𝖩',
        'K': '𝖪', 'L': '𝖫', 'M': '𝖬', 'N': '𝖭', 'O': '𝖮', 'P': '𝖯', 'Q': '𝖰', 'R': '𝖱', 'S': '𝖲', 'T': '𝖳',
        'U': '𝖴', 'V': '𝖵', 'W': '𝖶', 'X': '𝖷', 'Y': '𝖸', 'Z': '𝖹'
    },
    "Dotted Style": {
        'A': 'Ä', 'B': 'Ḅ', 'C': 'Ċ', 'D': 'Ḋ', 'E': 'Ë', 'F': 'Ḟ', 'G': 'Ġ', 'H': 'Ḧ', 'I': 'Ï', 'J': 'J̈',
        'K': 'K̈', 'L': 'L̈', 'M': 'M̈', 'N': 'N̈', 'O': 'Ö', 'P': 'P̈', 'Q': 'Q̈', 'R': 'R̈', 'S': 'S̈', 'T': 'T̈',
        'U': 'Ü', 'V': 'V̈', 'W': 'Ẅ', 'X': 'Ẍ', 'Y': 'Ÿ', 'Z': 'Z̈'
    },
    "Double Line": {
        'A': '𝔸', 'B': '𝔹', 'C': 'ℂ', 'D': '𝔻', 'E': '𝔼', 'F': '𝔽', 'G': '𝔾', 'H': 'ℍ', 'I': '𝕀', 'J': '𝕁',
        'K': '𝕂', 'L': '𝕃', 'M': '𝕄', 'N': 'ℕ', 'O': '𝕆', 'P': 'ℙ', 'Q': 'ℚ', 'R': 'ℝ', 'S': '𝕊', 'T': '𝕋',
        'U': '𝕌', 'V': '𝕍', 'W': '𝕎', 'X': '𝕏', 'Y': '𝕐', 'Z': 'ℤ'
    },
    "Rock Style": {
        'A': 'Α', 'B': 'Β', 'C': 'Ͼ', 'D': 'Δ', 'E': 'Ε', 'F': 'Ϝ', 'G': 'Γ', 'H': 'Η', 'I': 'Ι', 'J': 'J',
        'K': 'Κ', 'L': 'Λ', 'M': 'Μ', 'N': 'Ν', 'O': 'Ο', 'P': 'Ρ', 'Q': 'Q', 'R': 'Я', 'S': 'Ѕ', 'T': 'Τ',
        'U': 'Υ', 'V': 'V', 'W': 'Ш', 'X': 'Χ', 'Y': 'Υ', 'Z': 'Ζ'
    },
    "Cute Style": {
        'A': 'ค', 'B': '๒', 'C': '¢', 'D': '∂', 'E': 'є', 'F': 'ғ', 'G': 'g', 'H': 'н', 'I': 'ι', 'J': 'נ',
        'K': 'к', 'L': 'ℓ', 'M': 'м', 'N': 'η', 'O': 'σ', 'P': 'ρ', 'Q': 'q', 'R': 'я', 'S': 'ѕ', 'T': 'т',
        'U': 'υ', 'V': 'ν', 'W': 'ω', 'X': 'χ', 'Y': 'у', 'Z': 'z'
    },
    "Fairy Style": {
        'A': 'ꋬ', 'B': 'ꃳ', 'C': 'ꉔ', 'D': 'ꃕ', 'E': 'ꏂ', 'F': 'ꊰ', 'G': 'ꁅ', 'H': 'ꃄ', 'I': 'ꀤ', 'J': 'ꀭ',
        'K': 'ꀗ', 'L': '꒒', 'M': 'ꂵ', 'N': 'ꋊ', 'O': 'ꄲ', 'P': 'ꉣ', 'Q': 'ꆰ', 'R': 'ꋪ', 'S': 'ꇙ', 'T': '꓄',
        'U': 'ꌈ', 'V': 'ꏝ', 'W': 'ꅐ', 'X': 'ꉧ', 'Y': 'ꌦ', 'Z': 'ꁴ'
    },
    "Magic Style": {
        'A': 'ᗩ', 'B': 'ᗷ', 'C': 'ᑕ', 'D': 'ᗪ', 'E': 'ᗴ', 'F': 'ᖴ', 'G': 'Ǥ', 'H': 'ᕼ', 'I': 'Ꭵ', 'J': 'ᒎ',
        'K': 'Ꮶ', 'L': 'Ꮭ', 'M': 'ᗰ', 'N': 'ᑎ', 'O': 'ᗝ', 'P': 'ᑭ', 'Q': 'Ɋ', 'R': 'ᖇ', 'S': 'ᔕ', 'T': 'Ꭲ',
        'U': 'ᑌ', 'V': 'ᐯ', 'W': 'ᗯ', 'X': '᙭', 'Y': 'Ƴ', 'Z': 'Ꮓ'
    },
    "Vintage Style": {
        'A': 'ꋫ', 'B': 'ꃃ', 'C': 'ꏸ', 'D': 'ꁕ', 'E': 'ꈼ', 'F': 'ꄘ', 'G': 'ꁍ', 'H': 'ꍩ', 'I': 'ꂑ', 'J': 'ꀭ',
        'K': 'ꀘ', 'L': 'ꀤ', 'M': 'ꂵ', 'N': 'ꋊ', 'O': 'ꂦ', 'P': 'ꉣ', 'Q': 'ꁸ', 'R': 'ꋪ', 'S': 'ꌗ', 'T': '꓄',
        'U': 'ꐇ', 'V': 'ꏯ', 'W': 'ꅏ', 'X': 'ꇒ', 'Y': 'ꐟ', 'Z': 'ꁴ'
    },
    "Elegant Script": {
        'A': '𝔸', 'B': '𝔹', 'C': 'ℂ', 'D': '𝔻', 'E': '𝔼', 'F': '𝔽', 'G': '𝔾', 'H': 'ℍ', 'I': '𝕀', 'J': '𝕁',
        'K': '𝕂', 'L': '𝕃', 'M': '𝕄', 'N': 'ℕ', 'O': '𝕆', 'P': 'ℙ', 'Q': 'ℚ', 'R': 'ℝ', 'S': '𝕊', 'T': '𝕋',
        'U': '𝕌', 'V': '𝕍', 'W': '𝕎', 'X': '𝕏', 'Y': '𝕐', 'Z': 'ℤ'
    },
    "Decorative": {
        'A': 'ꁲ', 'B': 'ꃴ', 'C': 'ꄲ', 'D': 'ꅉ', 'E': 'ꅦ', 'F': 'ꆄ', 'G': 'ꆭ', 'H': 'ꇎ', 'I': 'ꇺ',
        'J': 'ꈨ', 'K': 'ꉕ', 'L': 'ꉺ', 'M': 'ꊛ', 'N': 'ꊰ', 'O': 'ꋍ', 'P': 'ꋫ', 'Q': 'ꌈ', 'R': 'ꌣ',
        'S': 'ꍊ', 'T': 'ꍶ', 'U': 'ꎕ', 'V': 'ꎳ', 'W': 'ꏃ', 'X': 'ꏕ', 'Y': 'ꏝ', 'Z': 'ꏱ'
    },
    "Runes Alt": {
        'A': 'ᛆ', 'B': 'ᛒ', 'C': 'ᛍ', 'D': 'ᛑ', 'E': 'ᛂ', 'F': 'ᚠ', 'G': 'ᚵ', 'H': 'ᚻ', 'I': 'ᛁ', 'J': 'ᚤ',
        'K': 'ᚴ', 'L': 'ᛚ', 'M': 'ᛘ', 'N': 'ᚿ', 'O': 'ᚮ', 'P': 'ᛕ', 'Q': 'ᛩ', 'R': 'ᚱ', 'S': 'ᛋ', 'T': 'ᛐ',
        'U': 'ᚢ', 'V': 'ᚡ', 'W': 'ᚥ', 'X': 'ᛪ', 'Y': 'ᚣ', 'Z': 'ᛨ'
    },
    "Old English": {
        'A': '𝔄', 'B': '𝔅', 'C': 'ℭ', 'D': '𝔇', 'E': '𝔈', 'F': '𝔉', 'G': '𝔊', 'H': 'ℌ', 'I': 'ℑ', 'J': '𝔍',
        'K': '𝔎', 'L': '𝔏', 'M': '𝔐', 'N': '𝔑', 'O': '𝔒', 'P': '𝔓', 'Q': '𝔔', 'R': 'ℜ', 'S': '𝔖', 'T': '𝔗',
        'U': '𝔘', 'V': '𝔙', 'W': '𝔚', 'X': '𝔛', 'Y': '𝔜', 'Z': 'ℨ'
    },
    "Stylish Dots": {
        'A': '𝒶', 'B': '𝒷', 'C': '𝒸', 'D': '𝒹', 'E': '𝑒', 'F': '𝒻', 'G': '𝑔', 'H': '𝒽', 'I': '𝒾', 'J': '𝒿',
        'K': '𝓀', 'L': '𝓁', 'M': '𝓂', 'N': '𝓃', 'O': '𝑜', 'P': '𝓅', 'Q': '𝓆', 'R': '𝓇', 'S': '𝓈', 'T': '𝓉',
        'U': '𝓊', 'V': '𝓋', 'W': '𝓌', 'X': '𝓍', 'Y': '𝓎', 'Z': '𝓏'
    },
    "Handwriting": {
        'A': '𝒜', 'B': 'ℬ', 'C': '𝒞', 'D': '𝒟', 'E': 'ℰ', 'F': 'ℱ', 'G': '𝒢', 'H': 'ℋ', 'I': 'ℐ', 'J': '𝒥',
        'K': '𝒦', 'L': 'ℒ', 'M': 'ℳ', 'N': '𝒩', 'O': '𝒪', 'P': '𝒫', 'Q': '𝒬', 'R': 'ℛ', 'S': '𝒮', 'T': '𝒯',
        'U': '𝒰', 'V': '𝒱', 'W': '𝒲', 'X': '𝒳', 'Y': '𝒴', 'Z': '𝒵'
    },
    "Fancy Bold": {
        'A': '𝓐', 'B': '𝓑', 'C': '𝓒', 'D': '𝓓', 'E': '𝓔', 'F': '𝓕', 'G': '𝓖', 'H': '𝓗', 'I': '𝓘', 'J': '𝓙',
        'K': '𝓚', 'L': '𝓛', 'M': '𝓜', 'N': '𝓝', 'O': '𝓞', 'P': '𝓟', 'Q': '𝓠', 'R': '𝓡', 'S': '𝓢', 'T': '𝓣',
        'U': '𝓤', 'V': '𝓥', 'W': '𝓦', 'X': '𝓧', 'Y': '𝓨', 'Z': '𝓩'
    },
    "Antique": {
        'A': 'ꍏ', 'B': 'ꌃ', 'C': 'ꉓ', 'D': 'ꀸ', 'E': 'ꍟ', 'F': 'ꎇ', 'G': 'ꁅ', 'H': 'ꃅ', 'I': 'ꀤ', 'J': 'ꀭ',
        'K': 'ꀘ', 'L': '꒒', 'M': 'ꎭ', 'N': 'ꈤ', 'O': 'ꂦ', 'P': 'ᖘ', 'Q': 'ꆰ', 'R': 'ꋪ', 'S': 'ꌗ', 'T': '꓄',
        'U': 'ꀎ', 'V': 'ᐯ', 'W': 'ꅏ', 'X': 'ꊼ', 'Y': 'ꌩ', 'Z': 'ꁴ'
    },
    "Mystic": {
        'A': 'Ꭿ', 'B': 'Ᏸ', 'C': 'Ꮳ', 'D': 'Ꭰ', 'E': 'Ꭼ', 'F': 'Ꮀ', 'G': 'Ꮆ', 'H': 'Ꮒ', 'I': 'Ꭵ', 'J': 'Ꮰ',
        'K': 'Ꮶ', 'L': 'Ꮭ', 'M': 'Ꮇ', 'N': 'Ꮑ', 'O': 'Ꭷ', 'P': 'Ꮲ', 'Q': 'Ꭴ', 'R': 'Ꮢ', 'S': 'Ꮥ', 'T': 'Ꮦ',
        'U': 'Ꮼ', 'V': 'Ꮙ', 'W': 'Ꮗ', 'X': 'Ꮂ', 'Y': 'Ꮍ', 'Z': 'Ꮓ'
    },
    "Squared": {
        'A': '🄰', 'B': '🄱', 'C': '🄲', 'D': '🄳', 'E': '🄴', 'F': '🄵', 'G': '🄶', 'H': '🄷', 'I': '🄸', 'J': '🄹',
        'K': '🄺', 'L': '🄻', 'M': '🄼', 'N': '🄽', 'O': '🄾', 'P': '🄿', 'Q': '🅀', 'R': '🅁', 'S': '🅂', 'T': '🅃',
        'U': '🅄', 'V': '🅅', 'W': '🅆', 'X': '🅇', 'Y': '🅈', 'Z': '🅉'
    },
    "Circled Neg": {
        'A': '🅐', 'B': '🅑', 'C': '🅒', 'D': '🅓', 'E': '🅔', 'F': '🅕', 'G': '🅖', 'H': '🅗', 'I': '🅘', 'J': '🅙',
        'K': '🅚', 'L': '🅛', 'M': '🅜', 'N': '🅝', 'O': '🅞', 'P': '🅟', 'Q': '🅠', 'R': '🅡', 'S': '🅢', 'T': '🅣',
        'U': '🅤', 'V': '🅥', 'W': '🅦', 'X': '🅧', 'Y': '🅨', 'Z': '🅩'
    }
}

def transform_text(text, style_map):
    """Transform text using the given style map."""
    result = ""
    for char in str(text).upper():
        if char.isspace():
            result += " "
        elif char.isalpha():
            if char in style_map:
                result += style_map[char]
            else:
                result += char
        else:
            result += char
    return result

def style_name(name, style_type, style_name_str):
    """Style a name using the specified style type and name."""
    try:
        if not name:
            return "Please provide a name to style"
            
        if style_type == "text":
            if style_name_str not in STYLE_MAPS:
                logger.error(f"Style {style_name_str} not found in STYLE_MAPS")
                return name
            return transform_text(name, STYLE_MAPS[style_name_str])
        elif style_type == "normal":
            if style_name_str not in NORMAL_FONTS:
                logger.error(f"Style {style_name_str} not found in NORMAL_FONTS")
                return name
            return NORMAL_FONTS[style_name_str].replace("NAME", name)
        else:  # fancy
            if style_name_str not in FANCY_FONTS:
                logger.error(f"Style {style_name_str} not found in FANCY_FONTS")
                return name
            return FANCY_FONTS[style_name_str].replace("NAME", name)
    except Exception as e:
        logger.error(f"Error styling name: {e}")
        return name 