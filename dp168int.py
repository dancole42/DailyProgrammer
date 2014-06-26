def get_unit_count(job_site, unit_breakdown={}):
	for unit in job_site:
		if unit_breakdown.has_key(unit):
			unit_breakdown[unit] += 1
		else:
			unit_breakdown[unit] = 1
	del unit_breakdown['\n']
	return unit_breakdown

def get_unit_area(job_site, area):
	units = get_unit_count(job_site)
	for unit_count in units:
		units[unit_count] = (units[unit_count], units[unit_count] * area)
	return units

def print_report(job_site, area):
	job_site = get_unit_area(job_site, area)
	for unit in job_site:
		print '%s: Total SF (%s), Total Units: %s' % (unit, job_site[unit][1], job_site[unit][0] )

if __name__ == '__main__':
	reddit_job = """ooooooooooooooooooooooDDDDDooooooooooooooooooooooooooooo
ooooooooooooooooooooooDDDDDooooooooooooooooooooooooooooo
ooo##################o#####o#########################ooo
o@o##################o#####o#########################ooo
ooo##################o#####o#########################oTo
o@o##################################################ooo
ooo##################################################oTo
o@o############ccccccccccccccccccccccc###############ooo
pppppppppppppppcOOOOOOOOOOOOOOOOOOOOOc###############oTo
o@o############cOBBBBBBBBBBBBBBBBBBBOc###############ooo
ooo####V#######cOBBBBBBBBBBBBBBBBBBBOc###############oTo
o@o####V#######cOBBBBBBBBBBBBBBBBBBBOc###############ooo
ooo####V#######cOBBBBBBBBBBBBBBBBBBBOcpppppppppppppppppp
o@o####V#######cOBBBBBBBBBBBBBBBBBBBOc###############ooo
ooo####V#######cOBBBBBBBBBBBBBBBBBBBOc######v########oTo
o@o####V#######cOBBBBBBBBBBBBBBBBBBBOc######v########ooo
ooo####V#######cOOOOOOOOOOOOOOOOOOOOOc######v########oTo
o@o####V#######ccccccccccccccccccccccc######v########ooo
ooo####V#######ppppppppppppppppppppppp######v########oTo
o@o############ppppppppppppppppppppppp###############ooo
oooooooooooooooooooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooooooooooooooooooo"""

	area = 100
	print_report(reddit_job, area)