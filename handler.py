#!/usr/bin/env python
from mackerel.clienthde import Client, MackerelClientError
import json


def handler(event, context):
    filename = event.get('filename')

    if filename is None:
        print "Filename is required"
        return "error"

    with open(filename) as data_file:
        data = json.load(data_file)

    # Create Mackerel client
    mackerel_client = Client(mackerel_api_key=data['mackerel_api_key'])

    # Update Monitors
    try:
        monitor_ids = []
        # Retrieve list of monitors from Mackerel
        for monitor in data['monitors']:
            monitor_ids.append(monitor['mackerel_monitor_id'])
        monitors = mackerel_client.get_monitors(ids=monitor_ids)

        for monitor in data['monitors']:
            params = monitor['parameters']
            monitor_id = monitor['mackerel_monitor_id']
            obj = monitors[monitor_id]

            # Check existence
            if obj is None:
                print "Monitor ID %s not found" % monitor_id
                continue

            # Update based on params
            for param in params:
                key = param['key']
                if param['type'] == "replace":
                    value = param['value']
                    setattr(obj, key, value)
                elif param['type'] == "remove":
                    setattr(obj, key, None)
                else:
                    print "Type is not recognized"

            # Send to Mackerel
            mackerel_client.update_monitor(
                monitor_id=monitor_id,
                monitor_params=obj._to_post_params_dict()
            )
    except MackerelClientError:
        raise

    return "finished"
