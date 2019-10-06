import pandas as pd


def main():
	"""
	This program unwrangles finra representative data to be easier to work
	with in Tableau.
	"""

	# Load df
	df = pd.read_pickle('finra_reps_df.pkl')

	# Only keep one current employer and one previous employer for
	# ease-of-use in Tableau
	drop_cols = [
		'CrntEmp_1',
		'EmpHss_1', 'EmpHss_2', 'EmpHss_3', 'EmpHss_4', 'EmpHss_5',
		'EmpHss_6', 'EmpHss_7', 'EmpHss_8', 'EmpHss_9', 'EmpHss_10',
		'EmpHss_11', 'EmpHss_12', 'EmpHss_13', 'EmpHss_14', 'EmpHss_15'
	]
	df = df.drop(columns=drop_cols)

	# Break up cols like Current Employer from dict to distinct cols
	# Current Employer
	df = pd.concat(
		[df.drop(['CrntEmp_0'], axis=1), df['CrntEmp_0'].apply(pd.Series)], axis=1
	)
	df = df.rename(
		index=str,
		columns={
			'city': 'Current Employer City',
			'cntry': 'Current Employer Country',
			'orgNm': 'Current Employer Name',
			'orgPK': 'Current Employer ID',
			'postlCd': 'Current Employer Postal Code',
			'state': 'Current Employer State',
			'str1': 'Current Employer Address 1',
			'str2': 'Current Employer Address 2'
		}
	)
	# Previous Employer
	df = pd.concat(
		[df.drop(['EmpHss_0'], axis=1), df['EmpHss_0'].apply(pd.Series)],
		axis=1
	)
	df = df.rename(
		index=str,
		columns={
			'city': 'Previous Employer City',
			'fromDt': 'Previous Employer Start Date',
			'orgNm': 'Previous Employer Name',
			'state': 'Previous Employer State',
			'toDt': 'Previous Employer End Date'
		}
	)
	# Exm_0
	df = pd.concat(
		[df.drop(['Exm_0'], axis=1), df['Exm_0'].apply(pd.Series)],
		axis=1
	)
	df = df.rename(index=str, columns={'exmCd': 'Exam 1'})
	df = df.drop(columns=['exmDt', 'exmNm'])
	# Exm_1
	df = pd.concat(
		[df.drop(['Exm_1'], axis=1), df['Exm_1'].apply(pd.Series)],
		axis=1
	)
	df = df.rename(index=str, columns={'exmCd': 'Exam 2'})
	df = df.drop(columns=['exmDt', 'exmNm'])
	# Exm_2
	df = pd.concat(
		[df.drop(['Exm_2'], axis=1), df['Exm_2'].apply(pd.Series)],
		axis=1
	)
	df = df.rename(index=str, columns={'exmCd': 'Exam 3'})
	df = df.drop(columns=['exmDt', 'exmNm'])

	# Rename columns in general for pretty print in Tableau
	df = df.rename(
		index=str,
		columns={
			'actvAGReg': 'Active Registration',
			'firstNm': 'First Name',
			'indvlPK': 'Individual ID',
			'lastNm': 'Last Name',
			'midNm': 'Middle Name',
			'sufNm': 'Name Suffix',
			'hasBankrupt': 'Has Bankrupt',
			'hasBond': 'Has Bond',
			'hasCivilJudc': 'Has Civil Judc',
			'hasCriminal': 'Has Criminal',
			'hasCustComp': 'Has Customer Complaint',
			'hasInvstgn': 'Has Investigation',
			'hasJudgment': 'Has Judgement',
			'hasRegAction': 'Has Regulatory Action',
			'hasTermination': 'Has Termination'
		}
	)

	# Map 'Y' to True, 'N' to false for relevant columns
	df = df.replace({
		'Active Registration': {'Y': True, 'N': False},
		'Has Bankrupt': {'Y': True, 'N': False},
		'Has Bond': {'Y': True, 'N': False},
		'Has Civil Judc': {'Y': True, 'N': False},
		'Has Criminal': {'Y': True, 'N': False},
		'Has Customer Complaint': {'Y': True, 'N': False},
		'Has Investigation': {'Y': True, 'N': False},
		'Has Judgement': {'Y': True, 'N': False},
		'Has Regulatory Action': {'Y': True, 'N': False},
		'Has Termination': {'Y': True, 'N': False},
	})

	# Keep 0's in the beginning of relevant columns
	df['Individual ID'] = df['Individual ID'].astype('str')
	df['Current Employer ID'] = df['Current Employer ID'].astype('str')
	df['Current Employer Postal Code'] = \
		df['Current Employer Postal Code'].astype('str')

	# Name formatting
	df['First Name'] = df['First Name'].apply(lambda name: name.capitalize())
	df['Last Name'] = df['Last Name'].apply(lambda name: name.capitalize())
	df['Middle Name'] = df['Middle Name'].astype('str')
	df['Middle Name'] = df['Middle Name'].apply(lambda name: name.capitalize())

	# Output
	df.to_csv('finra_reps_tableau.csv', index=False)


if __name__ == '__main__':
	main()
