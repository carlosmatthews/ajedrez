import React, { Component } from 'react';
import Tablero, {representacion_pieza, es_mov_posible} from './Tablero';

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
    fetch('/tablero')
      .then(response => response.json())
      .then(data => {
        const tablero = {}
        for (const p of data) {
          const pos = [p[0], p[1]];
          const pieza = [p[2], p[3]];
          tablero[pos] = pieza;
        }
        console.log("Tablero cargado");
        this.setState({tablero: tablero});
      });
  }

  click_casillero(f,c) {
    const state = this.state;
    const tablero = state.tablero;
    const pieza = tablero[[f,c]];
    if (pieza && pieza[1] === state.quien_juega) {
      this.setState({
        pieza_seleccionada: pieza,
        pos_seleccionada: [f,c],
        mov_posibles: [],
      });
      fetch(`/movimientos?fila=${f}&col=${c}`)
        .then(response => response.json())
        .then(data => {
          if (data.error) {
            console.error(data.error);
            return;
          }
          this.setState({mov_posibles: data});
        });
      return;
    }

    const nuevo_state = {
      pieza_seleccionada: null,
      pos_seleccionada: null,
      mov_posibles: [],
    }
    if (state.pos_seleccionada) {
      //if (es_mov_posible(state.mov_posibles, [f,c])) {
      if (true) {
        const pieza_original = tablero[state.pos_seleccionada];
        delete tablero[state.pos_seleccionada];
        tablero[[f,c]] = pieza_original;
        nuevo_state.tablero = tablero;
        nuevo_state.quien_juega = otro_color(state.quien_juega);
      }
    }
    this.setState(nuevo_state);

  }

  render() {
    const state=this.state;
    return <>
      <table>
        <tbody>
          <tr id="main_column">
            <td id="tableroTD">
              <Tablero tablero={state.tablero}
                mov_posibles={state.mov_posibles}
                pos_seleccionada={state.pos_seleccionada}
                click={this.click_casillero}/>
            </td>
            <td id="infoTD">
              <h1>Juegan {state.quien_juega === 'B' ? 'BLANCAS' : 'NEGRAS'}</h1>
              {state.pieza_seleccionada && <>
                <h3>Pieza Seleccionada: <span className="pieza">{representacion_pieza(state.pieza_seleccionada)}</span></h3>
              </>}  
            </td>
          </tr>
        </tbody>
      </table>
    </>;
  }
}

const otro_color = (color) => color === 'B' ? 'N' : 'B';

export default Partida;
