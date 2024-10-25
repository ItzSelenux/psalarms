import argparse
from psalarms import
(
	alarmmgr_add,
	alarmmgr_list,
	alarmmgr_remove,
	alarmmgr_edit
)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Portable Synchronized Alarms")
	parser.add_argument("--new", nargs=1, help="Add alarms with format DDMMAA/HHMMSS/id")
	parser.add_argument("--list", nargs=1, help="List alarms for specific ID")
	parser.add_argument("--remove", nargs=1, help="Remove alarms for specific ID/sub_id")
	parser.add_argument("--edit", nargs=1, help="Edit alarm with format DDMMAA/HHMMSS/id/sub_id")

	args = parser.parse_args()

	if args.new:
		try:
			date_str, time_str, alarm_id = args.new[0].split('/')
			alarmmgr_add(date_str, time_str, alarm_id)
		except ValueError:
			print("Incorrect format. Please use DDMMAA/HHMMSS/id to add an alarm.")
	elif args.list:
		alarm_id = args.list[0]
		alarmmgr_list(alarm_id)
	elif args.remove:
		ids = args.remove[0].split('/')
		alarm_id = ids[0]
		sub_id = int(ids[1]) if len(ids) > 1 else None
		alarmmgr_remove(alarm_id, sub_id)
	elif args.edit:
		try:
			new_date_str, new_time_str, alarm_id, sub_id = args.edit[0].split('/')
			sub_id = int(sub_id)
			alarmmgr_edit(alarm_id, sub_id, new_date_str, new_time_str)
		except ValueError:
			print("Incorrect format. Please use DDMMAA/HHMMSS/id/sub_id to edit an alarm.")
	else:
		parser.print_help()