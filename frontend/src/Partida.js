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
      jugador: 'B',
    }
    this.click_casillero = this.click_casillero.bind(this);
  }

  componentDidMount() {this.cargar_tablero();}

  parse_partida_response(data) {
    console.log(data);
    const tablero = {}
    for (const p of data.tablero) {
      const pos = [p[0], p[1]];
      const pieza = [p[2], p[3]];
      tablero[pos] = pieza;
    }
    this.setState({
      tablero: tablero,
      jugador: data.jugador,
      continua_juego: data.continua_juego,
      ganador: data.ganador,
      mov_posibles: [],
    });
    console.log("Partida cargada");
  }

  cargar_tablero() {
    fetch('/partida')
      .then(response => response.json())
      .then(data => {
        this.parse_partida_response(data)
      })
  }

  click_casillero(f,c) {
    const state = this.state;
    const tablero = state.tablero;
    const pieza = tablero[[f,c]];
    if (pieza && pieza[1] === state.jugador) {
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
            alert(data.error);
            return;
          }
          this.setState({mov_posibles: data.mov_posibles});
        });
      return;
    }

    if (state.pos_seleccionada) {
      const f0 = this.state.pos_seleccionada[0];
      const c0 = this.state.pos_seleccionada[1];
      fetch(`/mover?fila=${f0}&col=${c0}&fila2=${f}&col2=${c}`)
        .then(response => response.json())
        .then(data => {
          console.log(data);
          if (data.error) {
            console.error(data.error);
            alert(data.error);
            return;
          }
          this.parse_partida_response(data);
          this.setState({
            pieza_seleccionada: null,
            pos_seleccionada: null,
            mov_posibles: [],
          });
        });
    }
    //   //if (es_mov_posible(state.mov_posibles, [f,c])) {
    //   if (true) {
    //     const pieza_original = tablero[state.pos_seleccionada];
    //     delete tablero[state.pos_seleccionada];
    //     tablero[[f,c]] = pieza_original;
    //     nuevo_state.tablero = tablero;
    //     nuevo_state.jugador = otro_color(state.jugador);
    //   }
    // }
//    this.setState(nuevo_state);

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
              <h1>Juegan {state.jugador === 'B' ? 'BLANCAS' : 'NEGRAS'}</h1>
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
