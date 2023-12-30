import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar as ℏ

fontsize = 16

# Problem a

def E(l, m, α, β):
    return α*ℏ*l*(l+1) + β*ℏ*m

α = 1
β_α_ratio = np.linspace(0, 8, 100)
for l in range(4):
    for m in range(-l,l+1):
        β = β_α_ratio * α
        plt.plot(β_α_ratio, E(l,m,α,β)/(α*ℏ), label = r'$|${: },{: }$\rangle$'.format(l,m))
        if l == 3:
            break

plt.xlabel(r'$\beta/\alpha$', fontsize=fontsize)
plt.ylabel(r'$E/[\alpha\hbar]$', fontsize=fontsize)
plt.title(r'Energy of $|l,m\rangle$ states as a function of $\beta/\alpha$', fontsize=fontsize)
plt.legend(loc = 3, ncol = 2)
plt.savefig('a.pdf')
plt.show()


# Problem b

β_α_ratio = [i for i in range(4)]
colors = ['red', 'green', 'purple', 'magenta']
for ratio in β_α_ratio:
    l = np.floor(ratio)    
    m = -l
    width = 2
    α = 1
    plt.hlines(m, 2*l, 2*l + width, label=r'$L_z$ = {: }'.format(int(m)), color = colors[int(l)])
    
for ratio in β_α_ratio:
    l = np.floor(ratio)
    plt.scatter([(l+1)*2,(l+1)*2], [-l,-l-1], color = colors[int(l)], label=r'$L_z$ = {: } & $L_z$ = {: }'.format(int(-l), int(-l-1)))
    

plt.xlabel(r'$β/α$', fontsize=fontsize)
plt.xticks([i for i in range(0,9,2)])
plt.ylabel(r'$L_z [ℏ]$', fontsize=fontsize)
plt.title(r'$L_z$ of the groundstate as a function of $β/α$', fontsize=fontsize)
plt.legend(loc = 3, ncol = 2)
plt.savefig('b.pdf')
plt.show()

# Problem g

θ = np.linspace(0, np.pi, 100)
P = 3/8 * np.sin(θ)*(2 - np.sin(θ)**2)
P = P/sum(P)

plt.plot(θ, P)
print(P.max())
index1, index2 = np.where(P == P.max())[0]
print(index1, index2)
plt.scatter(θ[index1], P[index1], color = 'red', label = r'$θ_{max_1}$', zorder=2)
plt.scatter(θ[index2], P[index2], color = 'green', label = r'$θ_{max_2}$', zorder=2)

plt.title(r"Probability distribution of $|ψ\rangle$", fontsize=fontsize)
plt.xlabel(r'$θ$ [rad]', fontsize=fontsize)
plt.ylabel(r'$P(θ)$', fontsize=fontsize)
plt.xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'])

print(f'Most probable angles are {θ[index1]: .4f} and {θ[index2]: .4f} radians, or {θ[index1]*180/np.pi: .4f} and {θ[index2]*180/np.pi: .4f} degrees.')

plt.legend()
plt.savefig('g.pdf')
plt.show()