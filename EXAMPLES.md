# Configuration Examples

Real-world configuration examples for different users and preferences.

## Example 1: UK New Balance Fan

**User Profile**: Prefers dark colors, UK size 12.5, budget-conscious

**Interactive Setup Answers**:
- Brand: New Balance
- Size: UK 12.5
- Location: United Kingdom (GBP)
- Budget: Under £100
- Colors: Black, Grey/Neutral tones, Navy/Dark blue
- Interested in: 9060, 2002R, 990, 574
- Avoid: Fresh Foam models

**Resulting settings.json**:
```json
{
  "configured": true,
  "manufacturer": "New Balance",
  "size": "UK 12.5",
  "maxPrice": 100,
  "currency": "GBP",
  "location": "UK",
  "colorPreferences": {
    "preferred": ["black", "grey", "dark blue"],
    "accents": ["metallic tones welcome"],
    "avoid": ["white-dominant", "bright colors"]
  },
  "goodExamples": ["9060", "2002R", "990", "574"],
  "modelsToAvoid": ["Fresh Foam"]
}
```

## Example 2: US Nike Sneakerhead

**User Profile**: Loves classic Nike silhouettes, US size 10, willing to spend more

**Interactive Setup Answers**:
- Brand: Nike
- Size: US 10
- Location: United States (USD)
- Budget: Under $200
- Colors: Black, White, Grey/Neutral tones, Bold/Bright colors
- Interested in: Air Max 90, Dunk Low, Jordan 1, Air Force 1
- Avoid: Revolution, Tanjun

**Resulting settings.json**:
```json
{
  "configured": true,
  "manufacturer": "Nike",
  "size": "US 10",
  "maxPrice": 200,
  "currency": "USD",
  "location": "US",
  "colorPreferences": {
    "preferred": ["black", "white", "grey", "bold colors"],
    "accents": ["any"],
    "avoid": []
  },
  "goodExamples": ["Air Max 90", "Dunk Low", "Jordan 1", "Air Force 1"],
  "modelsToAvoid": ["Revolution", "Tanjun"],
  "retailers": [
    {
      "name": "Nike US",
      "url": "https://www.nike.com",
      "regions": ["US"]
    },
    {
      "name": "Foot Locker US",
      "url": "https://www.footlocker.com",
      "regions": ["US"]
    },
    {
      "name": "Finish Line",
      "url": "https://www.finishline.com",
      "regions": ["US"]
    }
  ]
}
```

## Example 3: EU Adidas Minimalist

**User Profile**: Clean aesthetic, EU size 44, loves retro models

**Interactive Setup Answers**:
- Brand: Adidas
- Size: EU 44
- Location: Europe/EU (EUR)
- Budget: Under €120
- Colors: White, Grey/Neutral tones, Earth tones
- Interested in: Samba, Gazelle, Campus, Spezial
- Avoid: None

**Resulting settings.json**:
```json
{
  "configured": true,
  "manufacturer": "Adidas",
  "size": "EU 44",
  "maxPrice": 120,
  "currency": "EUR",
  "location": "EU",
  "colorPreferences": {
    "preferred": ["white", "grey", "beige", "off-white", "cream"],
    "accents": ["subtle earth tones"],
    "avoid": ["neon", "bright colors"]
  },
  "goodExamples": ["Samba", "Gazelle", "Campus", "Spezial"],
  "modelsToAvoid": [],
  "retailers": [
    {
      "name": "Adidas EU",
      "url": "https://www.adidas.eu",
      "regions": ["EU"]
    },
    {
      "name": "END Clothing",
      "url": "https://www.endclothing.com",
      "regions": ["UK", "EU", "US"]
    },
    {
      "name": "Zalando",
      "url": "https://www.zalando.com",
      "regions": ["EU"]
    }
  ]
}
```

## Example 4: UK Vans Skater

**User Profile**: Skateboarder, UK size 9, prefers dark colors, tight budget

**Interactive Setup Answers**:
- Brand: Vans
- Size: UK 9
- Location: United Kingdom (GBP)
- Budget: Under £75
- Colors: Black, Navy/Dark blue
- Interested in: Old Skool, Sk8-Hi, Half Cab
- Avoid: Slip-ons (needs lace support)

**Resulting settings.json**:
```json
{
  "configured": true,
  "manufacturer": "Vans",
  "size": "UK 9",
  "maxPrice": 75,
  "currency": "GBP",
  "location": "UK",
  "colorPreferences": {
    "preferred": ["black", "navy", "dark grey"],
    "accents": ["white stripe OK"],
    "avoid": ["bright colors", "patterns"]
  },
  "goodExamples": ["Old Skool", "Sk8-Hi", "Half Cab"],
  "modelsToAvoid": ["Slip-On", "Era"],
  "retailers": [
    {
      "name": "Vans UK",
      "url": "https://www.vans.co.uk",
      "regions": ["UK"]
    },
    {
      "name": "Size?",
      "url": "https://www.size.co.uk",
      "regions": ["UK"]
    },
    {
      "name": "JD Sports",
      "url": "https://www.jdsports.co.uk",
      "regions": ["UK"]
    }
  ]
}
```

## Example 5: US Running Enthusiast

**User Profile**: Serious runner, needs performance shoes, US size 11.5

**Interactive Setup Answers**:
- Brand: Nike (or Asics, Brooks)
- Size: US 11.5
- Location: United States (USD)
- Budget: Under $150
- Colors: Any (performance > style)
- Interested in: Pegasus, Vaporfly, React
- Avoid: Lifestyle models (Revolution, Court)

**Resulting settings.json**:
```json
{
  "configured": true,
  "manufacturer": "Nike",
  "size": "US 11.5",
  "maxPrice": 150,
  "currency": "USD",
  "location": "US",
  "colorPreferences": {
    "preferred": [],
    "accents": ["any - performance matters"],
    "avoid": []
  },
  "goodExamples": ["Pegasus", "Vaporfly", "React", "Zoom Fly"],
  "modelsToAvoid": ["Revolution", "Court", "SB"],
  "includeShipping": true,
  "retailers": [
    {
      "name": "Nike US",
      "url": "https://www.nike.com",
      "regions": ["US"]
    },
    {
      "name": "Running Warehouse",
      "url": "https://www.runningwarehouse.com",
      "regions": ["US"]
    },
    {
      "name": "Dick's Sporting Goods",
      "url": "https://www.dickssportinggoods.com",
      "regions": ["US"]
    }
  ]
}
```

## Example 6: Multi-Brand Deal Hunter

**User Profile**: Flexible on brand, loves deals, UK size 10

**Interactive Setup Answers**:
- Brand: Other → "Nike, Adidas, New Balance, Puma"
- Size: UK 10
- Location: United Kingdom (GBP)
- Budget: Under £100
- Colors: All selected (Black, White, Grey, Navy, Earth tones)
- Interested in: Classic silhouettes
- Avoid: Budget lines (Advantage, Revolution, Fresh Foam)

**Resulting settings.json**:
```json
{
  "configured": true,
  "manufacturer": "Nike|Adidas|New Balance|Puma",
  "size": "UK 10",
  "maxPrice": 100,
  "currency": "GBP",
  "location": "UK",
  "colorPreferences": {
    "preferred": ["any neutral or classic colors"],
    "accents": ["acceptable"],
    "avoid": ["only extreme neons"]
  },
  "goodExamples": ["Air Max", "Samba", "9060", "Suede Classic"],
  "modelsToAvoid": ["Advantage", "Revolution", "Fresh Foam"],
  "retailers": [
    {
      "name": "Size?",
      "url": "https://www.size.co.uk",
      "regions": ["UK"]
    },
    {
      "name": "JD Sports",
      "url": "https://www.jdsports.co.uk",
      "regions": ["UK"]
    },
    {
      "name": "Foot Locker UK",
      "url": "https://www.footlocker.co.uk",
      "regions": ["UK"]
    },
    {
      "name": "ASOS",
      "url": "https://www.asos.com",
      "regions": ["UK"]
    }
  ]
}
```

## Tips for Customization

### Adding More Retailers

Edit the `retailers` array to include region-specific shops:

```json
{
  "name": "Retailer Name",
  "url": "https://www.retailer.com",
  "regions": ["UK", "EU"]
}
```

### Color Preferences

Be specific to get better matches:

```json
"colorPreferences": {
  "preferred": ["black", "charcoal", "dark navy", "forest green"],
  "accents": ["silver OK", "gum sole acceptable"],
  "avoid": ["all white", "neon pink", "bright orange"]
}
```

### Model Matching

Use partial matches for flexibility:

```json
"goodExamples": ["Air Max 90", "Air Max 95", "Air Max 97"],
"modelsToAvoid": ["Revolution", "Downshifter"]
```

The skill uses partial string matching, so "Air Max" will match all Air Max models.

## Advanced: Manual Editing

For power users who want complete control, directly edit `~/.claude/skills/shoescanner/settings.json`:

```bash
# Open in your preferred editor
nano ~/.claude/skills/shoescanner/settings.json

# Or use VS Code
code ~/.claude/skills/shoescanner/settings.json
```

Remember to set `"configured": true` after manual edits!
