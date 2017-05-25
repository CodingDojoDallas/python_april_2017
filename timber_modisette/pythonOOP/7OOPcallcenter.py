class Call(object):
	def __init__(self, unique_id, caller_name, caller_number, call_time, call_reason):
		self.unique_id = unique_id
		self.caller_name = caller_name
		self.caller_number = caller_number
		self.call_time = call_time
		self.call_reason = call_reason

	def displayAllAtts(self):
		print "unique id {}. name {}. number {}. time {}. reason {}."


class CallCenter(object):
	def __init__(self, calls=[]):
		self.calls = calls
		self.queue = len(self.calls)