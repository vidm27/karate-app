class Competitor {
    constructor(nombre, dojo, edad, categoria, cinturon, puntos) {
        this.nombre = nombre
        this.dojo = dojo
        this.edad = edad
        this.categoria = categoria
        this.cinturon = cinturon
        this.puntos = puntos
    }

    get totalPuntos() {
        return this.puntos.reduce((total, currentValue) => total + currentValue);
    }

    set nombre(value) {
        this._nombre = value
    }

    set dojo(value) {
        this._dojo = value
    }

    set edad(value) {
        this._edad = value
    }

    set categoria(value) {
        this._categoria = value
    }

    set cinturon(value) {
        this._cinturon = value
    }
}