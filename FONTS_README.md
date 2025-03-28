# Stylish Font Styles Collection

This is a comprehensive collection of stylish font variations that can be used for text decoration. Below are all the available font styles with examples:

## Available Font Styles

1. **Negative Circle** (🅗🅔🅔🅡)
   - Encircled letters with white fill
   - Example: 🅐🅑🅒🅓🅔

2. **Double Struck** (ℍ𝔼𝔼ℝ)
   - Mathematical double-struck letters
   - Used in mathematical notation

3. **Bold** (𝐇𝐄𝐄𝐑)
   - Bold letters with thick strokes
   - Clear and prominent appearance

4. **Bold Sans** (𝗛𝗘𝗘𝗥)
   - Bold sans-serif letters
   - Modern and clean look

5. **Bubble** (ⒽⒺⒺⓇ)
   - Letters enclosed in circles
   - Playful and decorative

6. **Negative Square** (🄷🄴🄴🅁)
   - Letters in white on black squares
   - High contrast appearance

7. **Monospace** (𝙷𝙴𝙴𝚁)
   - Fixed-width typewriter style
   - Technical appearance

8. **Math Bold** (𝝜𝝨𝝨𝝘)
   - Mathematical bold italic
   - Scholarly appearance

9. **Runic** (ꑛꍟꍟꋪ)
   - Ancient Germanic letters
   - Mystical appearance

10. **Japanese Style** (ん乇乇尺)
    - Letters styled like Japanese characters
    - Eastern aesthetic

11. **Cyrillic** (нєєя)
    - Russian alphabet style
    - Slavic appearance

12. **Wide** (ＨᗴＥᖇ)
    - Full-width letters
    - Expanded appearance

13. **Fancy Math** (𝔄𝔅ℭ𝔇)
    - Mathematical fraktur letters
    - Classical mathematical style

14. **Squared** (🅷🅴🅴🆁)
    - Letters in colored squares
    - Modern block style

15. **Script** (ℋℰℰℛ)
    - Cursive handwriting style
    - Elegant appearance

16. **Coptic** (ⲎⲈⲈⲄ)
    - Ancient Egyptian style
    - Historical appearance

17. **Ethiopic** (ዛꗛꗛɌ)
    - Ethiopian script style
    - African aesthetic

18. **Fancy Script** (ԋҽҽɾ)
    - Elegant cursive style
    - Decorative handwriting

19. **Ancient** (ᕼᘿᘿᖇ)
    - Old-style decorative letters
    - Antique appearance

20. **Medieval** (ℌ℮℮ℜ)
    - Gothic medieval style
    - Historical European style

21. **Mixed Style** (ɧɛɛཞ)
    - Combination of different styles
    - Eclectic appearance

22. **Decorative** (H̸̢E̶̡E̷̢R̵͢)
    - Letters with special effects
    - Glitch/distorted appearance

## Usage

Each font style can be accessed using the `font_styles.py` file. You can:

1. Get information about a specific font:
```python
info = get_font_info("Bold")
print(info["example"])  # Prints: 𝐇𝐄𝐄𝐑
```

2. List all available fonts:
```python
fonts = list_all_fonts()
for name, example in fonts:
    print(f"{name}: {example}")
```

## Notes

- Some fonts may not display correctly in all systems or applications
- Font rendering depends on Unicode support in the viewing platform
- Some styles may have limited character support 