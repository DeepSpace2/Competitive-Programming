# Solutions

## Python 3

```python
from datetime import datetime, timedelta

new_time = datetime.strptime(input(), '%H %M') - timedelta(minutes=45)
print('{} {}'.format(new_time.hour, new_time.minute))
```

Using `datetime.strptime` and `input()` to directly read the input as a `datetime` object and `timedelta` to calculate the `45` minutes offset. Then simply using `str.format` to output in the required format. We could have used `datetime.strftime` but the output requires no-leading zeros and there is no such directive.