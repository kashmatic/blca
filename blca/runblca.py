import blca

def main():
	blca.blast_seq()
	blca.setup_msa()
	blca.run_muscle()
	blca.compute()
	blca.annotate()

if __name__ == "__main__":
	main()