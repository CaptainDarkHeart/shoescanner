# Installation Guide

## Quick Install

1. **Clone or download this repository**:
   ```bash
   git clone https://github.com/CaptainDarkHeart/shoescanner.git
   cd shoescanner
   ```

2. **Copy skill files to Claude's skills directory**:
   ```bash
   mkdir -p ~/.claude/skills/shoescanner
   cp skill/* ~/.claude/skills/shoescanner/
   ```

3. **Customize your preferences**:
   ```bash
   # Edit the settings file with your preferences
   nano ~/.claude/skills/shoescanner/settings.json
   # or use your preferred editor
   ```

4. **Use the skill in Claude Code**:
   ```
   /shoescanner
   ```

## Manual Installation

If you prefer to set it up manually:

1. Create the skill directory:
   ```bash
   mkdir -p ~/.claude/skills/shoescanner
   ```

2. Copy each file from the `skill/` directory:
   - `skill.json` - Skill metadata
   - `settings.json` - Configuration (customize this!)
   - `instructions.md` - Claude's instructions
   - `seen-deals.json` - Deal tracking
   - `README.md` - Documentation

3. Edit `~/.claude/skills/shoescanner/settings.json` to match your preferences.

## Configuration

### Required Settings

At minimum, update these in `settings.json`:

- `manufacturer` - Your preferred brand
- `size` - Your shoe size (include region: UK/US/EU)
- `maxPrice` - Maximum price you'll pay
- `location` - Your region (UK/US/EU)

### Example Configurations

#### UK New Balance Fan
```json
{
  "manufacturer": "New Balance",
  "size": "UK 12.5",
  "maxPrice": 105,
  "currency": "GBP",
  "location": "UK"
}
```

#### US Nike Enthusiast
```json
{
  "manufacturer": "Nike",
  "size": "US 10",
  "maxPrice": 150,
  "currency": "USD",
  "location": "US"
}
```

#### EU Adidas Collector
```json
{
  "manufacturer": "Adidas",
  "size": "EU 44",
  "maxPrice": 120,
  "currency": "EUR",
  "location": "EU"
}
```

## Verification

Test that the skill is installed correctly:

1. Open Claude Code
2. Type `/shoescanner`
3. The skill should load and begin searching

## Troubleshooting

### Skill not found
- Verify files are in `~/.claude/skills/shoescanner/`
- Check that `skill.json` exists and is valid JSON
- Restart Claude Code

### No results found
- Verify your `size` is correctly formatted (e.g., "UK 12.5", not just "12.5")
- Check that `location` matches retailers in the config
- Try increasing `maxPrice` to test
- Ensure `manufacturer` name matches what retailers use

### Duplicate deals
- The skill tracks seen deals in `seen-deals.json`
- To reset: `echo "[]" > ~/.claude/skills/shoescanner/seen-deals.json`

## Updating

To update the skill:

```bash
cd shoescanner
git pull
cp skill/* ~/.claude/skills/shoescanner/
```

Note: This will overwrite your `settings.json`, so back it up first!

```bash
cp ~/.claude/skills/shoescanner/settings.json ~/shoescanner-settings-backup.json
# ... update skill files ...
# ... restore your settings ...
```

## Support

- [GitHub Issues](https://github.com/CaptainDarkHeart/shoescanner/issues)
- [README](README.md)
- [Skill Documentation](skill/README.md)
