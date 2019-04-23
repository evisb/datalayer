import * as React from 'react'
import { Nav } from 'office-ui-fabric-react/lib/Nav'

export default class SideBar extends React.Component<any, any> {

  state = {
    groups: [{
      links: [{
        name: 'Datalayer',
        url: 'http://example.com',
        links: [{
          name: 'Activity',
          url: 'http://msn.com',
        }, {
          name: 'News',
          url: 'http://msn.com',
        }],
        isExpanded: true,
      }, {
        name: 'Documents',
        url: 'http://example.com',
        isExpanded: true,
      }, {
        name: 'Pages',
        url: 'http://msn.com',
      }, {
        name: 'Long Name Test for elipsis. Longer than 12em!',
        url: 'http://example.com',
      }, {
        name: 'Edit Link',
        url: 'http://example.com',
        iconClassName: 'ms-Icon--Edit',
      }, {
        name: 'Edit',
        url: '#',
        icon: 'Edit',
        onClick: () => {},
      }]
    }],
    expanded: 'expanded',
    collapsed: 'collapsed',
  }

  public constructor(props) {
    super(props)
  }

  public render() {
    const { groups, expanded, collapsed } = this.state
    return (
      <div className='SidebarMenu'>
        <Nav 
          groups={groups}
          expandedStateText={expanded}
          collapsedStateText={collapsed}
        />
      </div>
    )
  }

}
