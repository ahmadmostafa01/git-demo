import scrap_jobs
#newFeature
def titles():
    df = scrap_jobs.scrap()
    titles = df['Title'].tolist()
    return titles

if __name__ == '__main__':
    print(titles())
