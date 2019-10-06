import multiprocessing
import requests
import pandas as pd


def fetch(advisor_id):
	"""
	fetch() downloads the report of a financial advisor identified by advisor_id
	Note that the download may fail (likely because the data for that broker
	is no longer available online), in which case no error is raised but a simple
	failure statement is printed.

	:param advisor_id: int, identifier of advisor whose pdf report will be downloaded
	:return: None
	"""

	url = 'https://files.brokercheck.finra.org/individual/individual_{}.pdf'.format(advisor_id)
	print('Retrieving advisor #{}'.format(advisor_id))

	response = requests.get(url)

	if 'AccessDenied' not in response.text:
		with open('pdfs/{}.pdf'.format(advisor_id), 'wb') as pdf:
			pdf.write(response.content)
	else:
		print('Advisor #{} could not be downloaded'.format(advisor_id))


def main():
	"""
	This program uses multiprocessing to efficiently download reports
	of financial advisors
	"""

	# Ingest id's of advisors
	df = pd.read_csv('all_adviser_data.csv', usecols=['indvlPK'])
	advisor_ids = df['indvlPK']

	# Download report of financial advisors
	pool = multiprocessing.Pool(processes=8)
	pool_outputs = pool.map(fetch, advisor_ids)
	pool.close()
	pool.join()


if __name__ == '__main__':
	main()
