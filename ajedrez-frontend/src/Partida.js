import React, { Component } from 'react';
import Tablero, {representacion_pieza} from './Tablero';

class Partida extends Component {
  constructor(props) {
    super(props);
    this.click_casillero = this.click_casillero.bind(this);
    this.state = {
      tablero: null,
      mov_posibles: [],
      pos_seleccionada: null,
      pieza_seleccionada: null,
      quien_juega: 'B',
    }
    this.click_casillero = this.click_casillero.bind(this);
  }

  componentDidMount() {this.cargar_tablero();}

  cargar_tablero() {
    const tablero = {}; // TODO: llamar API de carli
    tablero[[1,0]] = ['P', 'B'];
    tablero[[1,1]] = ['P', 'B'];
    tablero[[0,0]] = ['T', 'B'];
    tablero[[0,1]] = ['C', 'B'];
    tablero[[0,2]] = ['A', 'B'];
    tablero[[0,3]] = ['RA', 'B'];
    tablero[[0,4]] = ['R', 'B'];

    tablero[[6,7]] = ['P', 'N'];
    tablero[[7,0]] = ['T', 'N'];
    tablero[[7,1]] = ['C', 'N'];
    tablero[[7,2]] = ['A', 'N'];
    tablero[[7,3]] = ['RA', 'N'];
    tablero[[7,4]] = ['R', 'N'];
    this.setState({tablero: tablero});
  }

  click_casillero(f,c) {
    const state = this.state;
    const tablero = state.tablero;
    const pieza = tablero[[f,c]];
    if (!state.pos_seleccionada) {
      if (pieza && pieza[1] === state.quien_juega) {
        this.setState({
          pieza_seleccionada: pieza,
          pos_seleccionada: [f,c],
        });
      }
    } else if (pieza && pieza[1] === state.quien_juega) {
      this.setState({
        pieza_seleccionada: pieza,
        pos_seleccionada: [f,c],
      });
    } else {
      //chequear if movimiento posible
      const pieza_original = tablero[state.pos_seleccionada];
      delete tablero[state.pos_seleccionada];
      tablero[[f,c]] = pieza_original;
      this.setState({
        pieza_seleccionada: null,
        pos_seleccionada: null,
        quien_juega: otro_color(state.quien_juega),
      });
      this.setState({})
    }
  }

  render() {
    const state=this.state;
    return <>
      <h3>Juega {state.quien_juega === 'B' ? 'BLANCAS' : 'NEGRAS'}</h3>
      <Tablero tablero={state.tablero}
               mov_posibles={state.mov_posibles}
               pos_seleccionada={state.pos_seleccionada}
               click={this.click_casillero}/>
      {state.pieza_seleccionada && <>
        <h3>Pieza Seleccionada: <span className="pieza">{representacion_pieza(state.pieza_seleccionada)}</span></h3>
        </>}
    </>;
  }
}

const otro_color = (color) => color === 'B' ? 'N' : 'B';

export default Partida;
