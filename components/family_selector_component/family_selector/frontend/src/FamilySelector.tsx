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
class FamilySelector extends StreamlitComponentBase {

  public state = {familias: this.props.args["familias"]}

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.

    const familias = this.state.familias

    const familias_disp = familias.map((fam: { [x: string]: any }, index: number) => {
      if (fam["selected"] === true) {
        return (
        <div>
          <div 
            style={{height:12,width:12,borderRadius:15,backgroundColor:fam["color"],display:"inline-block",cursor:'pointer'}}
            onClick={() => this.onClicked(familias, index)} >
          </div>
          <div style={{display:"inline-block", paddingLeft:10}}>
            {fam["name"]}
          </div>
        </div>
        )
      }
      else {
        return (
          <div>
            <div 
              style={{height:12,width:12,borderRadius:15,backgroundColor:"lightgray",display:"inline-block",}}
              onClick={() => this.onClicked(familias, index)} >
            </div>
            <div style={{display:"inline-block", paddingLeft:10}}>
              {fam["name"]}
            </div>
          </div>
        )
      }
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
      <div style={{maxWidth:250, minWidth:100, maxHeight:250, minHeight:80, margin:0, padding:0,backgroundColor:themeBackgroundColor,borderRadius:12}}>
        <div style={{maxHeight:'inherit', minHeight: 'inherit',overflowY:"scroll",borderRadius:10, paddingLeft:10,}}>
          {familias_disp}
        </div>
        <div style={{flexDirection:'row', display:'flex'}}>
          <div style={{...styleButton,borderTopLeftRadius:10, marginRight:2}} onClick={() => this.onSelect(false)}>
            <p style={{fontSize:15,textAlign:'center'}}>deselect all</p>
          </div>
          <div style={{...styleButton,borderTopRightRadius:10, marginLeft:2}} onClick={() => this.onSelect(true)}>
            <p style={{fontSize:15,textAlign:'center'}}>select all</p>
          </div>
        </div>
        <div style={{...styleButton,borderBottomRightRadius:10,borderBottomLeftRadius:10, marginTop:4}} onClick={() => this.onFilter(familias)}>
          <p style={{paddingLeft:15,fontSize:15,textAlign:'center',}}>filter</p>
        </div>
      </div>
    )
  }

  /** Click handler for our "Click Me!" button. */
  private onClicked = (familias: any, index:number) => {
    // Increment state.numClicks, and pass the new value back to
    // Streamlit via `Streamlit.setComponentValue`.
    familias[index]["selected"] = !familias[index]["selected"]
    this.setState({familias: familias})
    this.forceUpdate()
  }

  private onFilter = (familias: any) => {
    Streamlit.setComponentValue(familias)
    this.forceUpdate()
  }

  private onSelect = (bool: boolean) => {
    this.state.familias.forEach((fam:any) => {
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
export default withStreamlitConnection(FamilySelector)

