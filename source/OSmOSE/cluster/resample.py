import os
import argparse
import glob

import sox

def resample(*, input_dir: str, output_dir: str, target_fs: int, ind_min: int = 0, ind_max: int = -1):
    all_files = sorted(glob.glob(os.path.join(input_dir , '*wav')))
    
    # If ind_max is -1, we go to the end of the list.
    wav_list = all_files[ind_min:ind_max if ind_max != -1 else len(all_files)]

    tfm = sox.Transformer()
    tfm.set_output_format(rate=target_fs)

    for wav in wav_list:
        tfm.build_file(input_filepath=wav, output_filepath=os.path.join(output_dir, os.path.basename(wav)))

        print(f"{os.path.basename(wav)} resampled to {target_fs}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python script to resample a list of audio files using the sox tool. Does not change the file duration.")
    required = parser.add_argument_group('required arguments')
    required.add_argument("--input-dir", "-i", required=True, help="The input folder where the files to resample are.")
    required.add_argument("--output-dir", "-o", required=True, help="The output folder of the resampled files.")
    required.add_argument("--target-fs", "-fs", required=True, type=int, help="The target samplerate.")
    parser.add_argument("--ind-min", "-min", type=int, default=0, help="The first file to consider. Default is 0.")
    parser.add_argument("--ind-max", "-max", type=int, default=-1, help="The last file to consider. -1 means consider all files from ind-min. Default is -1")

    args = parser.parse_args()

    resample(input_dir=args.input_dir, output_dir=args.output_dir, target_fs=args.targets_fs, ind_min=args.ind_min, ind_max=args.ind_max)