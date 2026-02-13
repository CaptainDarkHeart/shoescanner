# Shoe Scanner Skill

An automated shoe deal finder that scans online retailers for shoes matching your exact preferences.

## Features

- 🔍 **Smart Filtering**: Searches by brand, size, price, and color preferences
- 🎯 **Model Targeting**: Specify good models and models to avoid
- 💰 **Price Tracking**: Set a max price threshold (with shipping included)
- 🌍 **Location-Aware**: Only checks retailers relevant to your region
- 📋 **Duplicate Prevention**: Tracks previously found deals to avoid repeats
- ⚙️ **Fully Customizable**: Easy JSON configuration for your preferences

## Installation

This skill is already installed at `~/.claude/skills/shoescanner/`

## Usage

Simply invoke the skill:
```
/shoescanner
```

The skill will scan configured retailers and report any new matches.

## Configuration

Edit `~/.claude/skills/shoescanner/settings.json` to customize your preferences:

```json
{
  "manufacturer": "New Balance",
  "size": "UK 12.5",
  "maxPrice": 105,
  "currency": "GBP",
  "location": "UK",
  "colorPreferences": {
    "preferred": ["black", "grey", "dark blue"],
    "accents": ["metallic tones welcome"],
    "avoid": ["white-dominant", "bright colors"]
  },
  "goodExamples": ["9060", "2002R", "990"],
  "modelsToAvoid": ["Fresh Foam"],
  "retailers": [...]
}
```

### Configuration Options

- **manufacturer**: Brand name (e.g., "New Balance", "Nike", "Adidas")
- **size**: Your shoe size with region (e.g., "UK 12.5", "US 10", "EU 44")
- **maxPrice**: Maximum price you're willing to pay
- **currency**: Currency code (GBP, USD, EUR)
- **location**: Your region (UK, US, EU) - determines which retailers to check
- **colorPreferences**:
  - `preferred`: Array of preferred colors
  - `accents`: Array of acceptable accent descriptions
  - `avoid`: Array of color patterns to avoid
- **goodExamples**: Model names/numbers you like
- **modelsToAvoid**: Model patterns to exclude (supports partial matching)
- **retailers**: List of retailers to check (with URLs and regions)
- **seenDealsFile**: Path to track found deals
- **includeShipping**: Whether to include shipping in price calculations

## Adding Retailers

To add more retailers, edit the `retailers` array in `settings.json`:

```json
{
  "name": "Retailer Name",
  "url": "https://www.retailer.com",
  "regions": ["UK", "EU"]
}
```

## Customization Examples

### For US Nike Fans
```json
{
  "manufacturer": "Nike",
  "size": "US 10",
  "maxPrice": 150,
  "currency": "USD",
  "location": "US",
  "goodExamples": ["Air Max", "Dunk", "Jordan 1"],
  "modelsToAvoid": ["Revolution", "Downshifter"]
}
```

### For EU Adidas Sneakerheads
```json
{
  "manufacturer": "Adidas",
  "size": "EU 44",
  "maxPrice": 120,
  "currency": "EUR",
  "location": "EU",
  "goodExamples": ["Samba", "Gazelle", "Campus"],
  "modelsToAvoid": []
}
```

## Output Example

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

## Files

- `skill.json` - Skill metadata
- `settings.json` - Your preferences (customize this!)
- `instructions.md` - Instructions for Claude
- `seen-deals.json` - Tracks previously found deals
- `README.md` - This file

## Tips

- Run the skill regularly to catch new deals and sales
- Update `goodExamples` as you discover models you like
- Add retailers specific to your region for better coverage
- Adjust `maxPrice` seasonally to catch sale events
- Check the `seen-deals.json` file to see your deal history

## Contributing

This skill is part of the [shoescanner project](https://github.com/CaptainDarkHeart/shoescanner).

## License

MIT
