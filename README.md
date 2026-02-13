# Shoe Scanner

An AI-powered shoe deal finder skill for Claude that automatically scans online retailers for shoes matching your exact preferences.

## Overview

Shoe Scanner is a Claude Code skill that helps you find great deals on shoes by automatically searching multiple retailers and filtering results based on your specific criteria: brand, size, price, color preferences, and model preferences.

**New to Shoe Scanner?** Check out the [Quick Start Guide](QUICKSTART.md) for a 2-minute setup!

## Features

- 🎤 **Interactive Setup**: First-run guided setup with simple questions - no config file editing required!
- 🔍 **Smart Filtering**: Automatically filters by brand, size, price, and color
- 🎯 **Model Targeting**: Specify favorite models and models to avoid
- 💰 **Price Tracking**: Set maximum price thresholds with shipping included
- 🌍 **Location-Aware**: Only checks retailers relevant to your region
- 📋 **Duplicate Prevention**: Tracks previously found deals
- ⚙️ **Fully Customizable**: Edit preferences anytime via JSON or re-run setup

## Installation

1. Clone this repository or copy the skill files to your Claude skills directory:
   ```bash
   cp -r ~/.claude/skills/shoescanner ~/.claude/skills/
   ```

2. Customize your preferences in `~/.claude/skills/shoescanner/settings.json`

3. Use the skill by typing `/shoescanner` in Claude Code

## Configuration

Edit `~/.claude/skills/shoescanner/settings.json` to match your preferences:

```json
{
  "manufacturer": "New Balance",
  "size": "UK 12.5",
  "maxPrice": 105,
  "currency": "GBP",
  "location": "UK",
  "colorPreferences": {
    "preferred": ["black", "grey", "dark blue", "dark green"],
    "accents": ["colorful accents OK", "metallic tones welcome"],
    "avoid": ["bright/loud colorways", "white-dominant"]
  },
  "goodExamples": ["1906", "9060", "2002R", "990"],
  "modelsToAvoid": ["Fresh Foam"]
}
```

### Configuration Options

| Option | Description | Example |
|--------|-------------|---------|
| `manufacturer` | Preferred brand | `"New Balance"`, `"Nike"`, `"Adidas"` |
| `size` | Your shoe size (with region) | `"UK 12.5"`, `"US 10"`, `"EU 44"` |
| `maxPrice` | Maximum price threshold | `105` |
| `currency` | Currency code | `"GBP"`, `"USD"`, `"EUR"` |
| `location` | Geographic region | `"UK"`, `"US"`, `"EU"` |
| `colorPreferences` | Color preferences object | See below |
| `goodExamples` | Models you like | `["9060", "2002R"]` |
| `modelsToAvoid` | Models to exclude | `["Fresh Foam"]` |
| `retailers` | List of retailers to check | See settings.json |

### Color Preferences

```json
"colorPreferences": {
  "preferred": ["black", "grey", "navy"],
  "accents": ["metallic acceptable", "subtle color pops OK"],
  "avoid": ["all white", "neon colors"]
}
```

## Usage

Simply invoke the skill in Claude Code:

```
/shoescanner
```

### First Time? No Problem!

On your first run, the skill will ask you a few simple questions:
- What brand? (Nike, Adidas, New Balance, etc.)
- What size? (UK/US/EU sizing)
- Where are you located?
- What's your budget?
- Color preferences? (optional)
- Any favorite or disliked models? (optional)

Your answers are saved automatically - no config file editing needed!

### How It Works

The skill will:
1. Load your saved preferences (or guide you through setup)
2. Search configured retailers for your region
3. Filter by size, price, color, and model preferences
4. Skip previously seen deals
5. Report new matches with direct purchase links

## Example Output

```
Found 2 new matches:

1. **New Balance 9060 - Black/Grey**
   - Price: £89.99 (free shipping)
   - Size: UK 12.5 in stock
   - Link: https://www.endclothing.com/...
   - Match: Dark colorway with grey accents, well under budget

2. **New Balance 2002R - Navy/Silver**
   - Price: £95.00 (free shipping)
   - Size: UK 12.5 available
   - Link: https://www.size.co.uk/...
   - Match: Dark blue with metallic accents, popular silhouette
```

## Supported Retailers (Default UK Configuration)

- New Balance UK
- Size?
- End Clothing
- JD Sports
- Foot Locker UK
- Offspring

You can add more retailers by editing the `retailers` array in `settings.json`.

## Customization Examples

### US Nike Configuration
```json
{
  "manufacturer": "Nike",
  "size": "US 10",
  "maxPrice": 150,
  "currency": "USD",
  "location": "US",
  "goodExamples": ["Air Max 90", "Dunk Low", "Jordan 1"],
  "modelsToAvoid": ["Revolution", "Downshifter"]
}
```

### EU Adidas Configuration
```json
{
  "manufacturer": "Adidas",
  "size": "EU 44",
  "maxPrice": 120,
  "currency": "EUR",
  "location": "EU",
  "goodExamples": ["Samba", "Gazelle", "Campus 00s"],
  "modelsToAvoid": []
}
```

**Want more examples?** See [EXAMPLES.md](EXAMPLES.md) for 6+ real-world configurations!

## How It Works

1. **Loads Configuration**: Reads your preferences from `settings.json`
2. **Searches Retailers**: Navigates to each retailer's website
3. **Filters Results**: Applies size, price, and availability filters
4. **Evaluates Matches**: Checks model names and colorways against your preferences
5. **Prevents Duplicates**: Compares against `seen-deals.json`
6. **Reports Findings**: Presents new matches with all relevant details
7. **Updates History**: Adds new matches to the seen deals file

## Files Structure

```
~/.claude/skills/shoescanner/
├── skill.json              # Skill metadata
├── settings.json           # Your preferences (customize this!)
├── instructions.md         # Instructions for Claude
├── seen-deals.json         # Previously found deals
└── README.md              # Documentation
```

## Tips

- **Run regularly**: Check for deals daily or weekly
- **Update preferences**: Refine your `goodExamples` as you discover new models
- **Add retailers**: Include region-specific retailers for better coverage
- **Adjust price**: Lower `maxPrice` during sale seasons for best deals
- **Review history**: Check `seen-deals.json` to track your findings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT

## Author

Built for Claude Code users who want to automate their shoe deal hunting.

## Documentation

- 📖 [Quick Start Guide](QUICKSTART.md) - Get up and running in 2 minutes
- 📦 [Installation Guide](INSTALL.md) - Detailed installation instructions
- 💡 [Configuration Examples](EXAMPLES.md) - Real-world user scenarios
- 🔧 [Skill README](skill/README.md) - Technical documentation

## Links

- [GitHub Repository](https://github.com/CaptainDarkHeart/shoescanner)
- [Report Issues](https://github.com/CaptainDarkHeart/shoescanner/issues)
