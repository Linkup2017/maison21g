odoo.define('pos_maison.models', function (require) {
    "use strict";

var { PosGlobalState } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');


const PosMaisonPosGlobalState = (PosGlobalState) => class PosMaisonPosGlobalState extends PosGlobalState {
    constructor(obj) {
        super(obj);
        this.pos_users = null;
        this.gender_selection = null;
    }
    async _processData(loadedData) {
        await super._processData(...arguments);
        if (this.config.module_pos_maison) {
            this.pos_users = loadedData['pos_users'];
            this.gender_selection = loadedData['gender_selection'];
        }
    }
}
Registries.Model.extend(PosGlobalState, PosMaisonPosGlobalState);

});
