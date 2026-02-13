# New Balance Shoe Scanner - Task Brief

## Target Specs
- **Size:** UK 12.5
- **Models:** Any New Balance model EXCEPT Fresh Foam series (sole wears out too quickly)
- **Good examples:** 1906, 9060, 1000 series, 574, 530, 550, 2002R, 990, 991, etc.
- **Avoid:** Fresh Foam anything (Fresh Foam X, Fresh Foam Arishi, Fresh Foam Roav, etc.)
- **Colors:** Dark colors preferred (black, grey, dark blue, dark green). Colorful accents OK. Metallic tones welcome.
- **Max Price:** £105 including shipping (UK delivery)
- **Avoid:** Bright/loud colorways, white-dominant shoes

## Sites to Check
1. **New Balance UK** - newbalance.co.uk (check sale section + main listings)
2. **Size?** - size.co.uk
3. **End Clothing** - endclothing.com
4. **JD Sports** - jdsports.co.uk
5. **Foot Locker UK** - footlocker.co.uk
6. **Offspring** - offspring.co.uk

## Process
1. Search each site for New Balance shoes
2. Filter to UK 12.5 availability
3. Filter to £100 or under
4. EXCLUDE any Fresh Foam models
5. Evaluate colorway against preferences
6. Check against seen-deals.json to avoid duplicates
7. Report any new matches

## Output
For each match, provide:
- Model name and colorway
- Price (note if shipping is extra)
- Direct link to product page
- Brief note on why it matches (color/style)

## Seen Deals File
Store found deals in: /Users/dantaylor/Claude/shoescanner/nb-seen-deals.json
Format: `{"url": "...", "found": "ISO date", "model": "...", "price": "..."}`
