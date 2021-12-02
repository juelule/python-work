tickets = [
  {
    "id": 1234,
    "violation_type": "Overtime Parking",
    "issue_date_utc": "2021-01-01 12:22:05",
    "feeincents": 2500,
    "amountpaid": 1000,
    "lpn": "lars"
  },
  {
    "id": 4312,
    "violation_type": "Parking on Curb",
    "issue_date_utc": "2021-01-09 23:45:02",
    "feeincents": 500,
    "amountpaid": 0,
    "lpn": "lars"
  },
  {
    "id": 8765,
    "violation_type": "Overtime Parking",
    "issue_date_utc": "2020-12-10 23:45:02",
    "feeincents": 3500,
    "amountpaid": 0,
    "lpn": "passpo"
  },
  {
    "id": 8271,
    "violation_type": "Handicap",
    "issue_date_utc": "2021-01-29 23:45:02",
    "feeincents": 10000,
    "amountpaid": 9000,
    "lpn": "lars"
  },
  {
    "id": 8730,
    "violation_type": "Meter Violation",
    "issue_date_utc": "2020-12-10 23:45:02",
    "feeincents": 1500,
    "amountpaid": 0,
    "lpn": "passpo"
  },
  {
    "id": 8572,
    "violation_type": "Parking on Curb",
    "issue_date_utc": "2021-02-01 23:45:02",
    "feeincents": 6500,
    "amountpaid": 0,
    "lpn": "ethan"
  },
  {
    "id": 9183,
    "violation_type": "Parking on Curb",
    "issue_date_utc": "2021-01-30 23:45:02",
    "feeincents": 300,
    "amountpaid": 0,
    "lpn": "lars"
  },
  {
    "id": 5827,
    "violation_type": "Parking on Curb",
    "issue_date_utc": "2021-01-10 23:45:02",
    "feeincents": 300,
    "amountpaid": 0,
    "lpn": "passpo"
  },
  {
    "id": 4563,
    "violation_type": "Parking on Curb",
    "issue_date_utc": "2021-01-22 23:45:02",
    "feeincents": 300,
    "amountpaid": 300,
    "lpn": "passpo"
  }
]

outstanding_list = [i["lpn"] for i in tickets if i["feeincents"] - i["amountpaid"] > 50]


greater_than_50 = dict((i,tickets.count(i)) for i in set(tickets))
