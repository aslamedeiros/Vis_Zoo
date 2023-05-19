import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode,  } from "react"

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class TypeSelector extends StreamlitComponentBase {

  public state = {types: this.props.args["types"]}

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.

    const types = this.state.types

    const type_disp = types.map((typ: { [x: string]: any }, index: number) => {
      var selectColor
      var name_display

      // name display
      if (typ['name'] === 'nan') {
        name_display = 'no type'
      }
      else{
        name_display = typ["name"]
      }

      // color display
      if (typ["selected"] === true) {
        selectColor = 'black'
      }
      else{
        selectColor = 'lightgray'
      }

      var styleShape
      styleShape = {height:12,width:12, display:'inline-block',cursor:'pointer'}
      if (typ["shape"] === 'circle') {
        styleShape = {...styleShape,borderRadius:15, backgroundColor:selectColor}
      }
      if (typ["shape"] === 'triangle') {
        styleShape = {
          width: 0,
          height: 0,
          backgroundColor: "transparent",
          borderStyle: "solid",
          borderTopWidth: 0,
          borderLeftWidth: 6,
          borderRightWidth: 6,
          borderBottomWidth: 12,
          borderLeftColor: "transparent",
          borderRightColor: "transparent",
          borderBottomColor: selectColor,
          display:'inline-block',
          cursor:'pointer'
        }
      }
      if (typ["shape"] === 'square'){
        styleShape = {...styleShape, backgroundColor:selectColor}
      }
      styleShape = {height:12,width:12, display:'inline-block',cursor:'pointer', backgroundColor:selectColor}

      return (
      <div>
        <div 
          style={{...styleShape}}
          onClick={() => this.onClicked(types, index)} >
        </div>
        <div style={{display:"inline-block", paddingLeft:10}}>
          {name_display}
        </div>
      </div>
      )
      }

      
    );

    const { theme } = this.props
    var primaryColor = "blue"
    var themeBackgroundColor = "blue"
     if (theme) {
      primaryColor = theme.primaryColor
      themeBackgroundColor = theme.secondaryBackgroundColor
     }

    const styleButton = {height:40, backgroundColor: primaryColor,paddingTop:10,flex:1,cursor:'pointer'}

    return (
      <div style={{maxWidth:250, minWidth:80, margin:0, padding:0,backgroundColor:themeBackgroundColor,borderRadius:12}}>
        <div style={{maxHeight:150, minHeight:50,overflowY:"scroll",borderRadius:10, paddingLeft:10,}}>
          {type_disp}
        </div>
        <div style={{flexDirection:'row', display:'flex'}}>
          <div style={{...styleButton,borderTopLeftRadius:10, marginRight:2}} onClick={() => this.onSelect(false)}>
            <p style={{fontSize:15,textAlign:'center'}}>deselect all</p>
          </div>
          <div style={{...styleButton,borderTopRightRadius:10, marginLeft:2}} onClick={() => this.onSelect(true)}>
            <p style={{fontSize:15,textAlign:'center'}}>select all</p>
          </div>
        </div>
        <div style={{...styleButton,borderBottomRightRadius:10,borderBottomLeftRadius:10, marginTop:4}} onClick={() => this.onFilter()}>
          <p style={{paddingLeft:15,fontSize:15,textAlign:'center',}}>filter</p>
        </div>
      </div>
    )
  }

  /** Click handler for our "Click Me!" button. */
  private onClicked = (types: any, index:number) => {
    // Increment state.numClicks, and pass the new value back to
    // Streamlit via `Streamlit.setComponentValue`.
    types[index]["selected"] = !types[index]["selected"]
    this.setState({types: types})
    this.forceUpdate()
  }

  private onFilter = () => {
    Streamlit.setComponentValue(this.state.types)
    this.forceUpdate()
  }

  private onSelect = (bool: boolean) => {
    this.state.types.forEach((fam:any) => {
      fam['selected'] = bool
    });
    this.forceUpdate()
  }

}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(TypeSelector)

