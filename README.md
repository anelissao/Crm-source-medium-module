# CRM Gravity Source & Medium

Odoo module that adds free-text Source and Medium fields to CRM leads with automatic UTM record creation.

## Features

- **Free-text input**: Enter source and medium as plain text instead of selecting from dropdowns
- **Auto-creation**: Automatically creates `utm.source` and `utm.medium` records if they don't exist
- **Smart matching**: Case-insensitive search to link existing UTM records
- **Real-time sync**: Updates standard `source_id` and `medium_id` fields automatically

## Installation

1. Copy the `crm_medium_source` folder to your Odoo addons directory
2. Update the apps list in Odoo
3. Install "CRM Gravity Source & Medium" from the Apps menu

## Dependencies

- `base`
- `crm`
- `utm`

## Usage

When creating or editing a CRM lead:

1. Navigate to the lead form
2. Find the "Source / Medium" section
3. Type source and medium names directly into the text fields
4. The module will:
   - Search for existing UTM records (case-insensitive)
   - Create new records if none exist
   - Link them to the lead automatically

## Technical Details

### New Fields

- `source_gravity` (Char): Free-text source field
- `medium_gravity` (Char): Free-text medium field

### Behavior

- **On change**: Searches for matching UTM records and links them
- **On create/write**: Creates missing UTM records and updates `source_id`/`medium_id`
- **Matching**: Case-insensitive name comparison using `=ilike`

## Version

1.0

## License

Odoo Proprietary License v1.0
