# Quick Start Guide

Get started with Shoe Scanner in under 2 minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/CaptainDarkHeart/shoescanner.git
cd shoescanner

# Install the skill
mkdir -p ~/.claude/skills/shoescanner
cp skill/* ~/.claude/skills/shoescanner/
```

## First Run

Open Claude Code and type:
```
/shoescanner
```

The skill will guide you through setup with 4-6 simple questions:

### 1. Brand Selection
```
What shoe brand are you looking for?
→ Nike
→ Adidas
→ New Balance
→ Vans
→ Other
```

### 2. Size Input
```
What's your shoe size?
→ US 9-11
→ US 11.5-13
→ UK 8-10
→ UK 10.5-12.5
→ EU 42-44
→ EU 45-47
→ Other (for custom size)
```

### 3. Location
```
Where are you located?
→ United Kingdom (GBP)
→ United States (USD)
→ Europe/EU (EUR)
→ Other
```

### 4. Budget
```
What's your maximum price budget?
→ Under £75 / $100 / €90
→ Under £100 / $150 / €120
→ Under £150 / $200 / €180
→ Under £200 / $250 / €230
→ Other (for custom amount)
```

### 5. Colors (Optional)
```
What colors do you prefer? (Select multiple)
→ Black
→ White
→ Grey/Neutral tones
→ Navy/Dark blue
→ Earth tones
→ Bold/Bright colors
```

### 6. Models (Optional)
```
Any specific models you're interested in?
(Type model names/numbers, or skip)

Any models you want to avoid?
(Type model names/numbers, or skip)
```

## That's It!

The skill will:
- ✅ Save your preferences automatically
- ✅ Search retailers in your region
- ✅ Find shoes matching your criteria
- ✅ Report new deals with direct links

## Next Time

Just type `/shoescanner` again - your preferences are saved!

## Update Preferences

Want to change your settings?

**Option 1: Manual Edit** (for advanced users)
```bash
nano ~/.claude/skills/shoescanner/settings.json
```

**Option 2: Reset and Re-run Setup**
```bash
# Set configured to false
echo '{"configured": false}' > ~/.claude/skills/shoescanner/settings.json
# Then run /shoescanner again
```

## Example Output

```
Found 2 new matches:

1. **Nike Air Max 90 - Black/White**
   - Price: $129.99 (free shipping)
   - Size: US 10 in stock
   - Link: https://www.nike.com/...
   - Match: Classic colorway, under budget

2. **Nike Dunk Low - Navy/Grey**
   - Price: $110.00 (free shipping)
   - Size: US 10 available
   - Link: https://www.footlocker.com/...
   - Match: Dark blue with neutral accents
```

## Tips

- Run `/shoescanner` regularly (daily/weekly) to catch new deals
- The skill remembers what it's already shown you (no duplicates!)
- Add more retailers by editing the settings file
- Refine your model preferences as you discover what you like

## Need Help?

- [Full README](README.md)
- [Installation Guide](INSTALL.md)
- [GitHub Issues](https://github.com/CaptainDarkHeart/shoescanner/issues)

Happy shoe hunting! 👟
