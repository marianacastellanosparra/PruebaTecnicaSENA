
import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api',
})

function App() {
  const [section, setSection] = useState('dashboard')
  const [assets, setAssets] = useState([])
  const [orders, setOrders] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [message, setMessage] = useState('')
  const [editingAsset, setEditingAsset] = useState(null)

  const [assetForm, setAssetForm] = useState({
    name: '',
    asset_type: '',
    location: '',
  })

  const [orderForm, setOrderForm] = useState({
    asset_id: '',
    title: '',
    description: '',
    priority: 'Media',
  })

  const loadData = async () => {
    setLoading(true)
    setError('')
    try {
      const [assetsResponse, ordersResponse] = await Promise.all([
        api.get('/assets'),
        api.get('/work-orders'),
      ])
      setAssets(assetsResponse.data)
      setOrders(ordersResponse.data)
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        'No fue posible conectar con el servidor. Verifica que el backend esté ejecutándose.'
      )
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    loadData()
  }, [])

  const notify = (text) => {
    setMessage(text)
    setTimeout(() => setMessage(''), 3500)
  }

  const handleAssetSubmit = async (event) => {
    event.preventDefault()
    setError('')
    try {
      if (editingAsset) {
        await api.put(`/assets/${editingAsset.id}`, assetForm)
        notify('Activo actualizado correctamente.')
      } else {
        await api.post('/assets', assetForm)
        notify('Activo registrado correctamente.')
      }
      setAssetForm({ name: '', asset_type: '', location: '' })
      setEditingAsset(null)
      await loadData()
    } catch (err) {
      setError(err.response?.data?.detail || 'No se pudo guardar el activo.')
    }
  }

  const editAsset = (asset) => {
    setEditingAsset(asset)
    setAssetForm({
      name: asset.name,
      asset_type: asset.asset_type,
      location: asset.location,
    })
    setSection('assets')
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  const deactivateAsset = async (asset) => {
    if (!window.confirm(`¿Deseas desactivar el activo "${asset.name}"?`)) return
    try {
      await api.patch(`/assets/${asset.id}/deactivate`)
      notify('Activo desactivado correctamente.')
      await loadData()
    } catch (err) {
      setError(err.response?.data?.detail || 'No se pudo desactivar el activo.')
    }
  }

  const handleOrderSubmit = async (event) => {
    event.preventDefault()
    setError('')
    try {
      await api.post('/work-orders', {
        ...orderForm,
        asset_id: Number(orderForm.asset_id),
      })
      setOrderForm({
        asset_id: '',
        title: '',
        description: '',
        priority: 'Media',
      })
      notify('Orden de trabajo creada correctamente.')
      await loadData()
    } catch (err) {
      setError(err.response?.data?.detail || 'No se pudo crear la orden.')
    }
  }

  const advanceOrder = async (order) => {
    const nextStatus = {
      Pendiente: 'En progreso',
      'En progreso': 'Finalizada',
    }[order.status]

    if (!nextStatus) return

    try {
      await api.patch(`/work-orders/${order.id}/status`, {
        status: nextStatus,
      })
      notify(`Orden actualizada: ${nextStatus}.`)
      await loadData()
    } catch (err) {
      setError(err.response?.data?.detail || 'No se pudo actualizar la orden.')
    }
  }

  const activeAssets = assets.filter((asset) => asset.status === 'Activo')
  const inactiveAssets = assets.length - activeAssets.length
  const pendingOrders = orders.filter((order) => order.status === 'Pendiente')
  const progressOrders = orders.filter((order) => order.status === 'En progreso')
  const finishedOrders = orders.filter((order) => order.status === 'Finalizada')

  const navItems = [
    { id: 'dashboard', label: 'Panel principal', icon: '▦' },
    { id: 'assets', label: 'Activos', icon: '▣' },
    { id: 'orders', label: 'Órdenes de trabajo', icon: '☷' },
  ]

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon">O</div>
          <div>
            <strong>ORION</strong>
            <span>MAINTENANCE LITE</span>
          </div>
        </div>

        <div className="menu-label">MENÚ PRINCIPAL</div>
        <nav>
          {navItems.map((item) => (
            <button
              key={item.id}
              className={`nav-item ${section === item.id ? 'selected' : ''}`}
              onClick={() => {
                setSection(item.id)
                setError('')
              }}
            >
              <span className="nav-icon">{item.icon}</span>
              {item.label}
            </button>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <span className="status-dot" />
          Sistema de mantenimiento
          <small>Versión 1.0</small>
        </div>
      </aside>

      <main className="main-content">
        <header className="topbar">
          <div>
            <span className="breadcrumb">ORION / </span>
            <strong>
              {navItems.find((item) => item.id === section)?.label}
            </strong>
          </div>
          <button className="refresh-button" onClick={loadData}>
            ↻ Actualizar
          </button>
        </header>

        <div className="page-content">
          <div className="welcome">
            <div>
              <p className="eyebrow">GESTIÓN DE MANTENIMIENTO</p>
              <h1>
                {section === 'dashboard' && 'Panel principal'}
                {section === 'assets' && 'Gestión de activos'}
                {section === 'orders' && 'Órdenes de trabajo'}
              </h1>
              <p className="subtitle">
                Administra los activos y las actividades de mantenimiento.
              </p>
            </div>
            <div className="date-label">
              {new Date().toLocaleDateString('es-CO', {
                day: '2-digit',
                month: 'long',
                year: 'numeric',
              })}
            </div>
          </div>

          {message && <div className="success-message">{message}</div>}
          {error && (
            <div className="error-message">
              {error}
              <button onClick={() => setError('')}>×</button>
            </div>
          )}

          {loading ? (
            <div className="loading">Cargando información...</div>
          ) : (
            <>
              {section === 'dashboard' && (
                <>
                  <div className="stats-grid">
                    <StatCard title="Total de activos" value={assets.length} icon="▣" />
                    <StatCard title="Activos disponibles" value={activeAssets.length} icon="✓" />
                    <StatCard title="Órdenes pendientes" value={pendingOrders.length} icon="◷" />
                    <StatCard title="Órdenes finalizadas" value={finishedOrders.length} icon="✓" />
                  </div>

                  <section className="panel">
                    <div className="panel-heading">
                      <div>
                        <h2>Órdenes recientes</h2>
                        <p>Últimas órdenes registradas en el sistema.</p>
                      </div>
                      <button className="text-button" onClick={() => setSection('orders')}>
                        Ver todas →
                      </button>
                    </div>
                    <OrderTable orders={orders.slice(0, 5)} />
                  </section>

                  <section className="panel">
                    <div className="panel-heading">
                      <div>
                        <h2>Resumen de activos</h2>
                        <p>Estado actual de los activos registrados.</p>
                      </div>
                      <button className="text-button" onClick={() => setSection('assets')}>
                        Ver activos →
                      </button>
                    </div>
                    <div className="summary-row">
                      <span>Activos</span>
                      <strong>{activeAssets.length}</strong>
                      <span>Inactivos</span>
                      <strong>{inactiveAssets}</strong>
                      <span>Órdenes en progreso</span>
                      <strong>{progressOrders.length}</strong>
                    </div>
                  </section>
                </>
              )}

              {section === 'assets' && (
                <>
                  <section className="panel form-panel">
                    <div className="panel-heading">
                      <div>
                        <h2>{editingAsset ? 'Editar activo' : 'Registrar nuevo activo'}</h2>
                        <p>Completa la información del activo.</p>
                      </div>
                    </div>
                    <form onSubmit={handleAssetSubmit} className="form-grid">
                      <label>
                        Nombre del activo
                        <input
                          required
                          maxLength="100"
                          placeholder="Ej. Computador oficina 01"
                          value={assetForm.name}
                          onChange={(e) => setAssetForm({ ...assetForm, name: e.target.value })}
                        />
                      </label>
                      <label>
                        Tipo de activo
                        <input
                          required
                          maxLength="50"
                          placeholder="Ej. Equipo informático"
                          value={assetForm.asset_type}
                          onChange={(e) => setAssetForm({ ...assetForm, asset_type: e.target.value })}
                        />
                      </label>
                      <label>
                        Ubicación
                        <input
                          required
                          maxLength="150"
                          placeholder="Ej. Oficina principal"
                          value={assetForm.location}
                          onChange={(e) => setAssetForm({ ...assetForm, location: e.target.value })}
                        />
                      </label>
                      <div className="form-actions">
                        <button className="primary-button" type="submit">
                          {editingAsset ? 'Guardar cambios' : '+ Registrar activo'}
                        </button>
                        {editingAsset && (
                          <button
                            className="secondary-button"
                            type="button"
                            onClick={() => {
                              setEditingAsset(null)
                              setAssetForm({ name: '', asset_type: '', location: '' })
                            }}
                          >
                            Cancelar
                          </button>
                        )}
                      </div>
                    </form>
                  </section>

                  <section className="panel">
                    <div className="panel-heading">
                      <div>
                        <h2>Activos registrados</h2>
                        <p>{assets.length} activos en total.</p>
                      </div>
                    </div>
                    <div className="table-wrapper">
                      <table>
                        <thead>
                          <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Tipo</th>
                            <th>Ubicación</th>
                            <th>Estado</th>
                            <th>Acciones</th>
                          </tr>
                        </thead>
                        <tbody>
                          {assets.map((asset) => (
                            <tr key={asset.id}>
                              <td>#{asset.id}</td>
                              <td className="table-name">{asset.name}</td>
                              <td>{asset.asset_type}</td>
                              <td>{asset.location}</td>
                              <td><StatusBadge status={asset.status} /></td>
                              <td>
                                <div className="actions">
                                  <button className="action-button" onClick={() => editAsset(asset)}>
                                    Editar
                                  </button>
                                  {asset.status === 'Activo' && (
                                    <button className="action-button danger" onClick={() => deactivateAsset(asset)}>
                                      Desactivar
                                    </button>
                                  )}
                                </div>
                              </td>
                            </tr>
                          ))}
                          {assets.length === 0 && <EmptyRow columns={6} />}
                        </tbody>
                      </table>
                    </div>
                  </section>
                </>
              )}

              {section === 'orders' && (
                <>
                  <section className="panel form-panel">
                    <div className="panel-heading">
                      <div>
                        <h2>Crear orden de trabajo</h2>
                        <p>Registra una nueva actividad de mantenimiento.</p>
                      </div>
                    </div>
                    <form onSubmit={handleOrderSubmit} className="form-grid">
                      <label>
                        Activo
                        <select
                          required
                          value={orderForm.asset_id}
                          onChange={(e) => setOrderForm({ ...orderForm, asset_id: e.target.value })}
                        >
                          <option value="">Selecciona un activo</option>
                          {activeAssets.map((asset) => (
                            <option key={asset.id} value={asset.id}>
                              #{asset.id} - {asset.name}
                            </option>
                          ))}
                        </select>
                      </label>
                      <label>
                        Título
                        <input
                          required
                          maxLength="120"
                          placeholder="Ej. Mantenimiento preventivo"
                          value={orderForm.title}
                          onChange={(e) => setOrderForm({ ...orderForm, title: e.target.value })}
                        />
                      </label>
                      <label>
                        Prioridad
                        <select
                          value={orderForm.priority}
                          onChange={(e) => setOrderForm({ ...orderForm, priority: e.target.value })}
                        >
                          <option>Baja</option>
                          <option>Media</option>
                          <option>Alta</option>
                        </select>
                      </label>
                      <label className="full-width">
                        Descripción
                        <textarea
                          required
                          placeholder="Describe el trabajo que se debe realizar..."
                          value={orderForm.description}
                          onChange={(e) => setOrderForm({ ...orderForm, description: e.target.value })}
                        />
                      </label>
                      <div className="form-actions">
                        <button className="primary-button" type="submit" disabled={activeAssets.length === 0}>
                          + Crear orden
                        </button>
                        {activeAssets.length === 0 && (
                          <span className="helper-text">Primero debes registrar un activo activo.</span>
                        )}
                      </div>
                    </form>
                  </section>

                  <section className="panel">
                    <div className="panel-heading">
                      <div>
                        <h2>Órdenes registradas</h2>
                        <p>{orders.length} órdenes en total.</p>
                      </div>
                    </div>
                    <OrderTable orders={orders} onAdvance={advanceOrder} />
                  </section>
                </>
              )}
            </>
          )}
        </div>
      </main>
    </div>
  )
}

function StatCard({ title, value, icon }) {
  return (
    <div className="stat-card">
      <div className="stat-icon">{icon}</div>
      <div>
        <p>{title}</p>
        <strong>{value}</strong>
      </div>
    </div>
  )
}

function StatusBadge({ status }) {
  const className = status?.toLowerCase().replaceAll(' ', '-') || ''
  return <span className={`status-badge ${className}`}>{status}</span>
}

function OrderTable({ orders, onAdvance }) {
  return (
    <div className="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Orden</th>
            <th>Activo</th>
            <th>Prioridad</th>
            <th>Estado</th>
            {onAdvance && <th>Acción</th>}
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td>#{order.id}</td>
              <td className="table-name">{order.title}</td>
              <td>{order.asset?.name || `Activo #${order.asset_id}`}</td>
              <td><span className={`priority ${order.priority?.toLowerCase()}`}>{order.priority}</span></td>
              <td><StatusBadge status={order.status} /></td>
              {onAdvance && (
                <td>
                  {order.status !== 'Finalizada' ? (
                    <button className="action-button" onClick={() => onAdvance(order)}>
                      {order.status === 'Pendiente' ? 'Iniciar' : 'Finalizar'}
                    </button>
                  ) : <span className="completed-text">Completada</span>}
                </td>
              )}
            </tr>
          ))}
          {orders.length === 0 && <EmptyRow columns={onAdvance ? 6 : 5} />}
        </tbody>
      </table>
    </div>
  )
}

function EmptyRow({ columns }) {
  return (
    <tr>
      <td colSpan={columns} className="empty-state">
        No hay registros para mostrar.
      </td>
    </tr>
  )
}

export default App
