import os
import glob
from pymol import pymol
from pymol import cmd 
from pymol import stored
import __main__
__main__.pymol_argv =[ 'pymol','-qc']
pymol.finish_launching()

def pdb_alignment(reference_pdb, mobile_pdb):
	'''Align two pdb structures and returns the results of values'''
	ref_name = os.path.splitext(os.path.basename(reference_pdb))[0]
	mob_name = os.path.splitext(os.path.basename(mobile_pdb))[0]
	cmd.load(reference_pdb)
	cmd.load(mobile_pdb)
	result = cmd.align(mob_name, ref_name)
	cmd.delete(ref_name)
	cmd.delete(mob_name)
	return result

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='RMSD calculation using Align function from PyMol')
	parser.add_argument('-PDB1', type=str, help='First protein structure')
	parser.add_argument('-PDB2', type=str, help='Second protein structure')
	args = parser.parse_args()
	reference = args.PDB1
	mobile = args.PDB2
	RMSD_after_refinement, atoms_after_refinement, refinement_cycles, RMSD_before_refinement, atoms_before_refinement, raw_alignment_score, residues_aligned = pdb_alignment(reference, mobile)
	print('RMSD after refinement: {0:.3f}\nNumber of aligned atoms after refinement: {1}\nNumber of refinement cycles: {2}\nRMSD before refinement: {3:.3f}\nNumber of aligned atoms before refinement: {4}\nRaw alignment score: {5}\nNumber of residues aligned: {6}'.format(RMSD_after_refinement, atoms_after_refinement, refinement_cycles, RMSD_before_refinement, atoms_before_refinement, raw_alignment_score, residues_aligned))