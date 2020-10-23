# crostab
### table and cross-table analytics

### Usage
```python
from crostab import Table
bistro_duty_roster = {
    'head': ['day', 'name', 'served', 'sold', 'adt'],
    'rows': [
        [1, 'Joyce', 70, 7, ''],
        [1, 'Lance', 98, 15, ''],
        [1, 'Naomi', 90, 14, ''],
    ]
}
table=Table.from_dict(bistro_duty_roster)
print(table.columns)
```