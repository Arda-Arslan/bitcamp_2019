import pandas as pd
import numpy as np


def helper(row):
	# Helper for .apply()
	return row['CrntEmp_0']['orgNm']


def main():
	"""
	This program ingests advisor data and calculates the ratio of the number of
	complaints advisors have received against them to the number of employees
	that work at a given organization.
	The idea is that organizations which tend to have a lot of employees
	with complaints made against them may be more nefarious and may be worth
	taking a closer look at.
	"""
	# Load data
	df = pd.read_pickle('all_adviser_data.pkl').reset_index(drop=True)

	# Determine whether advisor has complaint
	df['complaint'] = np.where(df['hasCustComp'] == 'Y', 1, 0)

	# Grab where every advisor currently works
	df['currEmpName'] = df.apply(helper, axis=1)

	# Perform calculations on complaints
	df = df.groupby('currEmpName')['complaint'].agg(['sum', 'count', 'mean'])

	# Rename columns for clarity
	df = df.rename(
		index=str,
		columns={
			'currEmpName': 'Current Employer Name',
			'sum': 'Number of Complaints',
			'count': 'Number of Employees',
			'mean': 'Complaints to Employees Ratio'
		}
	)

	# Sort
	df = df.sort_values(by='Number of Employees')
	df = df.reset_index()

	# Output
	df.to_csv('Employer Complaint Ratios.csv', index=False)


if __name__ == '__main__':
	main()
