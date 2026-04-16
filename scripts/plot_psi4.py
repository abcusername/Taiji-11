import numpy as np
import matplotlib.pyplot as plt
import os

file_m0 = "mp_Psi4_l2_m0_r100.00.asc"
file_m2 = "mp_Psi4_l2_m2_r100.00.asc"

def load_psi4(fname):
    data = np.loadtxt(fname)
    t = data[:, 0]
    re = data[:, 1]
    im = data[:, 2]
    amp = np.sqrt(re**2 + im**2)
    return t, re, im, amp

t0, re0, im0, amp0 = load_psi4(file_m0)
t2, re2, im2, amp2 = load_psi4(file_m2)

outdir = "psi4_results"
os.makedirs(outdir, exist_ok=True)

# 导出整理后的txt
np.savetxt(
    os.path.join(outdir, "l2_m0_psi4.txt"),
    np.column_stack((t0, re0, im0, amp0)),
    header="time RePsi4 ImPsi4 AbsPsi4"
)

np.savetxt(
    os.path.join(outdir, "l2_m2_psi4.txt"),
    np.column_stack((t2, re2, im2, amp2)),
    header="time RePsi4 ImPsi4 AbsPsi4"
)

# 图1：l=2,m=0
plt.figure(figsize=(10, 6))
plt.plot(t0, re0, label="Re(Psi4)")
plt.plot(t0, im0, label="Im(Psi4)")
plt.plot(t0, amp0, label="|Psi4|")
plt.xlabel("time")
plt.ylabel("Psi4")
plt.title("l=2, m=0")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(outdir, "l2_m0_psi4.png"), dpi=200)
plt.close()

# 图2：l=2,m=2
plt.figure(figsize=(10, 6))
plt.plot(t2, re2, label="Re(Psi4)")
plt.plot(t2, im2, label="Im(Psi4)")
plt.plot(t2, amp2, label="|Psi4|")
plt.xlabel("time")
plt.ylabel("Psi4")
plt.title("l=2, m=2")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(outdir, "l2_m2_psi4.png"), dpi=200)
plt.close()

# 图3：只比较振幅
plt.figure(figsize=(10, 6))
plt.plot(t0, amp0, label="l=2,m=0")
plt.plot(t2, amp2, label="l=2,m=2")
plt.xlabel("time")
plt.ylabel("|Psi4|")
plt.title("Psi4 amplitude comparison")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(outdir, "psi4_amp_compare.png"), dpi=200)
plt.close()

print("完成，结果保存在:", os.path.abspath(outdir))
