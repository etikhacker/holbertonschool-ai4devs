# Data Model - Smart Task Prioritizer

## Entity 1: Task
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier. |
| title | String | Task name. |
| deadline | Date | Due date. |
| effort | Integer | Difficulty (1-5). |
| priorityScore | Float | Calculated ranking value. |
| status | Enum | 'todo', 'doing', 'done'. |

## Entity 2: Category
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier. |
| name | String | Category name. |
| colorCode | String | Hex UI color. |

## Entity 3: UserSettings
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier. |
| themeMode | String | 'light' or 'dark'. |
| taskLimit | Integer | Max active tasks. |