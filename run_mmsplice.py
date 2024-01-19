import kipoi
import numpy as np

model = kipoi.get_model('MMSplice/pathogenicity')

for type_ in ['benign', 'pathogenic']:
    dl_kwargs = {'gtf': 'data/chr1.gtf.gz', 'fasta_file': 'data/chr1.fa', 'vcf_file': f'data/clinvar_chr1_{type_}.vcf.gz'}
    pred = model.pipeline.predict(dl_kwargs, batch_size=4)
    np.savetxt(f"pathogenicity_{type_}.csv", pred, delimiter=",")
