import csv

def write_log(logs, filename):
  """Writes a list of logs to a CSV file.

  Args:
    logs: A list of logs, where each log is a dictionary with keys 'timestamp',
      'level', 'message', and 'stack_trace'.
    filename: The name of the CSV file to write to.
  """

  with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'level', 'message', 'stack_trace']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for log in logs:
      writer.writerow(log)
