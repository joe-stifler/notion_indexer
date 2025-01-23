# notion_indexer

A Python library to index and traverse Notion workspaces, converting pages and databases into easily parsable formats like Markdown and Pandas DataFrames.

## Features

* **Traverse Notion Hierarchy:** Explore pages, databases, and blocks within a Notion workspace up to a specified depth.
* **Markdown Conversion:**  Transform Notion pages and databases into Markdown format for easy integration with other tools and platforms. Supports various block types including headings, lists, toggles, tables, and more.
* **DataFrame Representation:** Convert Notion databases into Pandas DataFrames for convenient data analysis and manipulation.
* **Filtering and Sorting:** Query databases with filters and sorts to retrieve specific data.
* **Easy-to-Use API:**  Simple and intuitive interface for interacting with Notion data.


## Installation

```bash
pip install notion-sdk pandas
pip install git+https://github.com/joe-stifler/notion_indexer.git # or clone and install locally
```

## Usage Basic Example

```python
from notion_indexer.notion_client import NotionClient
from notion_indexer.notion_reader import NotionReader
import os
from dotenv import load_dotenv

# Load Notion API key from .env file
load_dotenv()
integration_token = os.getenv("NOTION_API_KEY")

# Initialize NotionReader
reader = NotionReader(integration_token=integration_token)

# Load data from a Notion page or database URL
page_url = "https://www.notion.so/your-workspace/your-page-or-database-id"  # Replace with your actual URL
page_data = reader.load_data(page_url, max_depth=2)  # Adjust max_depth as needed


# Convert to Markdown
markdown_output = page_data.to_markdown()
print(markdown_output)


# If it's a database, convert to DataFrame
if hasattr(page_data, 'to_dataframe'):
    df = page_data.to_dataframe()
    print(df)


# Working with databases
database_url = "https://www.notion.so/your-workspace/your-database-id"
filter = {
    "property": "Status",  # Replace with your property name
    "select": {
        "equals": "In Progress"  # Replace with your filter value
    }
}
database_data = reader.load_data(database_url, max_depth=1, filter=filter)
df = database_data.to_dataframe()
print(df)
```

## Filtering and Sorting Databases

You can filter and sort the results when querying databases:

```json
filter = {
    "property": "Date",
    "date": {
        "on_or_after": "2024-01-01"
    }
}

sorts = [
    {
        "property": "Name",
        "direction": "ascending"
    }
]

database_data = reader.load_data(database_url, filter=filter, sorts=sorts)
```

## Contributing
Contributions are welcome! Feel free to open issues and submit pull requests.

## License

MIT

## Acknowledgements
Built using the Notion Python SDK.

Utilizes Pandas for DataFrame functionality.