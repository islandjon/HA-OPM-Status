class OPMStatusCard extends HTMLElement {
    set hass(hass) {
        const entityId = this.config.entity;
        const state = hass.states[entityId];
        const status = state.attributes.status;
        const postedDate = state.attributes.posted_date;
        const applicableDay = state.attributes.applicable_day;

        const now = new Date();
        const fivePM = new Date();
        fivePM.setHours(17, 0, 0, 0);

        let color = 'grey';
        let content = '?';

        if (new Date(applicableDay) > now && now.getHours() >= 17) {
            if (status === 'Open') {
                color = 'green';
                content = 'Open';
            } else if (status.includes('Delayed')) {
                color = 'yellow';
                content = status.split(' ')[1]; // Extract delay time
            } else {
                color = 'red';
                content = status;
            }
        }

        this.innerHTML = `
            <ha-card>
                <div class="card-content">
                    <div class="circle" style="background-color: ${color};">${content}</div>
                    <div>Status: ${status}</div>
                    <div>Posted: ${postedDate}</div>
                    <div>Applies to: ${applicableDay}</div>
                </div>
            </ha-card>
        `;
    }

    setConfig(config) {
        if (!config.entity) {
            throw new Error('You need to define an entity');
        }
        this.config = config;
    }

    getCardSize() {
        return 1;
    }
}

customElements.define('opm-status-card', OPMStatusCard);