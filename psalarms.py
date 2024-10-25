from tinydb import TinyDB, Query
from datetime import datetime
db = TinyDB('psalarms.json')

def alarmmgr_add(date_str, time_str, alarm_id):
	try:
		alarm_datetime = datetime.strptime(f"{date_str}/{time_str}", "%d%m%y/%H%M%S")
	except ValueError:
		print("Invalid date format. Please use DDMMAA/HHMMSS")
		return False

	Alarm = Query()
	existing_alarms = db.search(Alarm.id == alarm_id)
	sub_id = len(existing_alarms)

	db.insert
	({
		'id': alarm_id,
		'sub_id': sub_id,
		'date': date_str,
		'time': time_str,
		'datetime': alarm_datetime.isoformat()
	})
	print(f"Alarm '{alarm_id}' added: {date_str} {time_str}")
	return True

def alarmmgr_list(alarm_id):
	Alarm = Query()
	results = db.search(Alarm.id == alarm_id)

	if results:
		print(f"Alarms for ID '{alarm_id}':")
		for alarm in results:
			print(f"- Date: {alarm['date']} | Time: {alarm['time']}")
		return results
	else:
		print(f"No alarms found for ID '{alarm_id}'.")
		return []

def alarmmgr_remove(alarm_id, sub_id=None):
	Alarm = Query()
	if sub_id is not None:
		deleted = db.remove((Alarm.id == alarm_id) & (Alarm.sub_id == sub_id))
	else:
		deleted = db.remove(Alarm.id == alarm_id)
	
	if deleted:
		print(f"Deleted {len(deleted)} alarms with ID '{alarm_id}'" + (f" and Sub-ID '{sub_id}'." if sub_id else "."))
		return len(deleted)
	else:
		print(f"No alarms found with ID '{alarm_id}'" + (f" and Sub-ID '{sub_id}'." if sub_id else "."))
		return 0

def alarmmgr_edit(alarm_id, sub_id, new_date_str, new_time_str):
	try:
		new_alarm_datetime = datetime.strptime(f"{new_date_str}/{new_time_str}", "%d%m%y/%H%M%S")
	except ValueError:
		print("Invalid date format. Please use DDMMAA/HHMMSS")
		return False

	Alarm = Query()
	updated = db.update
	(
		{'date': new_date_str, 'time': new_time_str, 'datetime': new_alarm_datetime.isoformat()},
		(Alarm.id == alarm_id) & (Alarm.sub_id == sub_id)
	)

	if updated:
		print(f"Alarm '{alarm_id}' updated to: {new_date_str} {new_time_str}")
		return True
	else:
		print(f"No alarm found with ID '{alarm_id}' and Sub-ID '{sub_id}' to update.")
		return False