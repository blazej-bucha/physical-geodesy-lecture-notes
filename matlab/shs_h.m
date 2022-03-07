% Stiahnutie balíka "GrafLab" na výpočet sférické harmonického rozvoja
unzip("https://blazejbucha.com/graflab/GrafLab.zip", ".");

% Stiahnutie modelu topografie "DTM2006.0" do stupňa "360"
unzip("https://blazejbucha.com/graflab/test_data_GrafLab.zip", ".");

% Výpočet a zobrazenie zemskej topografie do rôznych stupňov "nmax"
for nmax = [30, 90, 360];

    GrafLab('OK', 1.0, 1.0, 0, nmax, [0 0 0 0 0], 'DTM2006.mat', 1, 0, ...
            -90.0, 0.25, 90, 0.0 ,0.25, 360.0, 0.0, ...
            [], [], [], [], ...
            char(sprintf("../figs/shs-topography/topography-nmax%d", ...
                         nmax)), ...
            0, 11, 1, [], 1, 0, 0, 2, 6, 1, 60, 600, 1);

end
