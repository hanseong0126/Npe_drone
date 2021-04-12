def change(usa,uae,jap,chi):
    usa_kind = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    usa_re = list()
    for i in usa_kind:
        usa_re.append(usa//i)
        usa = usa % i
    
    uae_kind = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    uae_re = list()
    for i in uae_kind:
        uae_re.append(uae//i)
        uae = uae % i

    jap_kind = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    jap_re = list()
    for i in jap_kind:
        jap_re.append(jap//i)
        jap = jap % i

    chi_kind = [100, 50, 20, 10, 5, 1, 0.5, 0.1]
    chi_re = list()
    for i in chi_kind:
        chi_re.append(chi//i)
        chi = chi % i
    
    total = [usa_re, uae_re, jap_re, chi_re]
    return total