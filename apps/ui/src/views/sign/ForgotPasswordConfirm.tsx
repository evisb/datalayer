import * as React from 'react'
import { connect } from 'react-redux'
import { ActionButton } from 'office-ui-fabric-react/lib/Button'
import IamApi from '../../api/iam/IamApi'
import history from '../../history/History'
import { mapDispatchToPropsConfig, mapStateToPropsConfig } from '../../actions/ConfigActions'

@connect(mapStateToPropsConfig, mapDispatchToPropsConfig)
export default class ForgotPasswordConfirm extends React.Component<any, any> {
  private readonly iamApi: IamApi

  public constructor(props) {
    super(props)
  }

  public render() {
    return (
      <div className='ms-fadeIn500 dla-padding20'>
        <div className='ms-fontSize-xxl'>Your password has been changed</div>
        <div style={{ height: '20px'}} />
        <div className="ms-Grid" style={{ padding: 0 }}>
          <div className="ms-Grid-row">
            <div className="ms-Grid-col ms-sm4 ms-md4 ms-lg4">
              <ActionButton
                iconProps={{ 
                  iconName: 'Home',
                }}
                disabled={false}
                checked={true}
                onClick={ e => { e.preventDefault(); history.push('/') }}
                >
                Home
              </ActionButton>
            </div>
            <div className="ms-Grid-col ms-sm8 ms-md8 ms-lg8 text-center">
              <img src="/img/explorer/explorer.svg"/>
            </div>
          </div>
        </div>
      </div>
    )
  }

}
