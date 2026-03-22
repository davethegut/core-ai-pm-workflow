---
name: html-reference-page
description: Generate polished, self-contained HTML reference pages with a professional dark theme. Use when creating stats pages, architecture docs, guides, or any shareable reference document.
---

# HTML Reference Page Skill

Generate polished, self-contained HTML reference pages. These pages are portable — anyone can open them in a browser with no dependencies.

## When to Use

- "Create a reference page for ..."
- "Make an HTML page about ..."
- "Build a stats page for ..."
- "Create a shareable doc for ..."

## Style Reference

### Design Tokens (CSS Variables)

```css
:root {
  --primary: #0077cc;
  --dark: #1b1b3a;
  --teal: #00bfb3;
  --bg: #f7f8fa;
  --card-bg: #ffffff;
  --text: #2c2c3e;
  --text-muted: #5a5a72;
  --border: #e2e4e9;
  --highlight: #eaf6ff;
}
```

### Required Structure

Every page must include:

1. **Dark gradient header** with badge, title (h1), and subtitle paragraph
2. **Container** (max-width: 960px, centered)
3. **Note block** (optional) — blue-left-bordered callout for context
4. **Sections** with h2 headings (blue bottom border)
5. **Cards** — white rounded boxes with content, tables, or descriptions
6. **Footer** — centered, muted text with purpose and data source

### Available Components

| Component | Class | Use For |
|-----------|-------|---------|
| Header badge | `.badge` | Category label |
| Info note | `.note` | Top-of-page context or disclaimers |
| Content card | `.card` | Case studies, feature descriptions, grouped data |
| Data table | `table` inside `.card` | Metric/value pairs, comparisons |
| Summary table | `.summary-table` | Full-width overview tables with dark headers |
| Resource link | `.resource-link` | Clickable link cards with title, description, URL |
| Tag | `.tag` / `.tag.blue` | Feature or category labels |
| Source citation | `.sources` | Attribution links below cards |

### Page Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PAGE TITLE</title>
  <style>
    /* Full CSS is self-contained — no external dependencies */
  </style>
</head>
<body>

<div class="header">
  <div class="container" style="padding-top:0;padding-bottom:0;">
    <span class="badge">BADGE TEXT</span>
    <h1>PAGE TITLE</h1>
    <p>Subtitle describing the page purpose.</p>
  </div>
</div>

<div class="container">

  <div class="note">
    Optional context note about data sources or scope.
  </div>

  <h2>Section Title</h2>

  <div class="card">
    <h3>Card Title</h3>
    <table>
      <tr><th>Metric</th><th>Value</th></tr>
      <tr><td>Description</td><td>Data</td></tr>
    </table>
    <p>Optional narrative context.</p>
    <div class="sources">
      <strong>Source:</strong>
      <a href="URL">Link text</a>
    </div>
  </div>

  <footer>
    Footer text &mdash; Audience &mdash; Data source note
  </footer>

</div>

</body>
</html>
```

## Process

1. **Understand the content** — What data, stats, or information needs to be presented?
2. **Choose components** — Cards for grouped items, summary tables for overviews, resource links for references
3. **Build the HTML** using the template structure above with full inline CSS
4. **Save to `output/html/`** with a descriptive filename
5. **Verify** — The page should be fully self-contained with no external dependencies

## Rules

- All CSS must be inline in a `<style>` tag — no external stylesheets
- All fonts must be system fonts — no Google Fonts or CDN loads
- No JavaScript unless absolutely necessary for the content
- No images — use HTML/CSS for all visual elements
- All external links must use `https://` URLs
- Include `@media print` styles for printability

## Output Location

Save all generated pages to `output/html/` with descriptive kebab-case filenames.
