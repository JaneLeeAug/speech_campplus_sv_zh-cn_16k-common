root@7f7912dd1ee1:/proj/gpu_mtk53732/3D-Speaker# python speakerlab/bin/infer_sv.py   --model_id /proj/gpu_mtk53732/speech_campplus_sv_zh-cn_16k-common  --wavs /proj/MR_dataset/mtk53732/SDSD0003640036.wav /proj/MR_dataset/mtk53732/SD/SD0002567077.wav
[INFO]: Use local model directory: /proj/gpu_mtk53732/speech_campplus_sv_zh-cn_16k-common
[INFO]: Matched official model id: iic/speech_campplus_sv_zh-cn_16k-common
/proj/gpu_mtk53732/3D-Speaker/speakerlab/bin/infer_sv.py:287: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  pretrained_state = torch.load(pretrained_model, map_location='cpu')
Traceback (most recent call last):
  File "/proj/gpu_mtk53732/3D-Speaker/speakerlab/bin/infer_sv.py", line 380, in <module>
    main()
  File "/proj/gpu_mtk53732/3D-Speaker/speakerlab/bin/infer_sv.py", line 287, in main
    pretrained_state = torch.load(pretrained_model, map_location='cpu')
  File "/opt/3dspeaker_venv/lib/python3.9/site-packages/torch/serialization.py", line 1114, in load
    return _legacy_load(
  File "/opt/3dspeaker_venv/lib/python3.9/site-packages/torch/serialization.py", line 1338, in _legacy_load
    magic_number = pickle_module.load(f, **pickle_load_args)
_pickle.UnpicklingError: invalid load key, 'v'.
