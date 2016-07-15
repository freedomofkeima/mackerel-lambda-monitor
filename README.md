mackerel-lambda-monitor
===============================

Mackerel is an integrated monitoring platform which is available at https://mackerel.io. This repository is created to provide an example how to update Monitoring rules in Mackerel dynamically.


Description
===============================


In each services, `mackerel_monitor_id` is required while `mackerel_monitor_name` will not be used in `handler.py` (easier identifier for human).

Each parameter in `parameters` has 3 possible values: `type`, `key`, and `value`. There are two kinds of `type`: `replace` and `remove`.

If `type` is `replace`, then you need to specify a pair of `key` (as specified in Mackerel [documentation](https://mackerel.io/api-docs/entry/monitors#create)) and `value`.

If `type` is `remove`, then you need to ensure that the specified `key` is an optional parameter (not a mandatory parameter). Otherwise, Mackerel will throw an error.

```
{
    "mackerel_monitor_id": "1ABcdEfghIj",
    "mackerel_monitor_name": "DynamoDB.ConsumedWriteCapacityUnits.users-table",
    "parameters": [
        {
            "type": "replace",
            "key": "warning",
            "value": 1000
        },
        {
            "type": "replace",
            "key": "critical",
            "value": 1200
        }
    ]
}
```


Development Libraries
===============================

- [mackerel.clienthde](https://github.com/HDE/py-mackerel-client)


Deployment
===============================

Each configuration file should have a pattern of `conf-*.json` (see `Makefile`). After that, you can specify which set of configuration rules should be executed at a specified time.

![Scheduled Role](https://raw.githubusercontent.com/freedomofkeima/mackerel-lambda-monitor/master/img/scheduled_rule.png)


Last Updated: July 15, 2016
