const apiUrl = 'https://api.safisense.com/api/v1/devices/uptime?company_id=apikirkcontainers&api_key=7EeFK8fnXsecJkSOSaYvJ98kF4YVPVHY';

fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        console.log('-------------------------------------');
        console.log('-------- API Kirk Containers --------');
        console.log('-------------------------------------\n');

        const ma = {};

        for (const i of data.data) {
            try {
                if (i.computedLoadStates.percentages.online >= 0) {
                    if (i.computedLoadStates.percentages.online > 0) {
                        ma[parseInt(i.deviceid.split('machine')[1])] = i.computedLoadStates.percentages.online;
                    } else {
                        ma[parseInt(i.deviceid.split('machine')[1])] = i.computedLoadStates.percentages.online;
                    }
                }
            } catch (error) {
                // error 
            }
        }

        const li = Object.keys(ma);

        for (const m of li.sort((a, b) => a - b)) {
            if (ma[m] > 0) {
                console.log(`\x1b[1;32m Machine ${m} is ${Math.round(ma[m] * 100)}% \x1b[0;0m`);
            } else {
                console.log(`\x1b[1;31m Machine ${m} is ${ma[m]}% \x1b[0;0m`);
            }
        }

        console.log('\n-------------------------------------');
    })
    .catch(error => {
        // error
        console.error(error);
    });
